import requests

import random
import time
from pathlib import Path
from time import sleep

from eth_account.signers.local import LocalAccount
from logzero import logger
from web3 import Account, Web3

import config

max_int = 115792089237316195423570985008687907853269984665640564039457584007913129639935


def approve(
    web3: Web3, token, spender, amount, wallet: LocalAccount, gas_multiplicator=2
):
    return call_function(
        token.functions.approve,
        wallet,
        web3,
        args=[spender, amount],
        gas_multiplicator=gas_multiplicator,
    )


def call_function(
    function,
    wallet: LocalAccount,
    w3: Web3,
    value=0,
    args=None,
    gas_multiplicator=None,
    tryes=config.ATTEMTS_TO_NODE_REQUEST,
):
    if args is None:
        args = []
    if gas_multiplicator is None:
        gas_multiplicator = 1
    tryNum = 0
    while True:
        gas_multiplicator += 1
        gas = w3.eth.estimate_gas(
            {
                "to": Web3.to_checksum_address(wallet.address),
                "from": Web3.to_checksum_address(wallet.address),
                "value": w3.to_wei(0.0001, "ether"),
            }
        ) + random.randint(50000, 100000)
        gas = int(gas * gas_multiplicator)
        dict_transaction = {
            "chainId": w3.eth.chain_id,
            "from": wallet.address,
            "value": w3.to_wei(value, config.NATIVE_DECIMALS),
            "gas": gas,
            "gasPrice": w3.eth.gas_price,
            "nonce": w3.eth.get_transaction_count(wallet.address),
        }
        logger.info(f"INFO | Calling {function.fn_name} .... attempt {tryNum + 1}")
        try:
            transaction = function(*args).build_transaction(dict_transaction)
            signed_txn = wallet.sign_transaction(transaction)

            wait_timings = config.WAIT_RECEIPT
            txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

            sleep(random.randint(random.randint(*wait_timings[0]), random.randint(*wait_timings[1])))
            receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
            sleep(random.randint(random.randint(*wait_timings[0]), random.randint(*wait_timings[1])))

            if receipt.status != 1:
                raise Exception("Failed Tx")
            logger.info(
                f"INFO | Successful called function {function.fn_name}\n {txn_hash.hex()}"
            )
            return receipt
        except Exception as e:
            tryNum += 1
            logger.error(f"ERROR | while calling {function.fn_name}.\n{e}")
            if tryNum > tryes:
                logger.error(f"ERROR | while calling {function.fn_name}.\n{e}")
                return False
            sleep(5)


def send_raw_transaction(w3, signed_txn):
    try:
        txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
        sleep(random.randint(random.randint(5, 7), random.randint(8, 10)))
        receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
        sleep(random.randint(random.randint(5, 7), random.randint(8, 10)))

        if receipt.status != 1:
            raise Exception("Failed Tx")

        logger.info(f"INFO | Successful sent tx:\n {txn_hash.hex()}")
        return receipt
    except Exception as e:
        logger.info(f"ERROR | while sending tx:\n{e}")
        raise e

def get(url, headers=None, params=None):
    if params is None:
        params = {}
    if headers is None:
        headers = {}
    tryNum = 0
    while True:
        try:
            r = requests.get(url, headers=headers, params=params)
            return r
        except Exception as e:
            tryNum += 1
            if tryNum > config.ATTEMTS_TO_API_REQUEST:
                logger.error(f"ERROR | Can't get response from {url}.\n{e}")
                raise e
            time.sleep(10)

def get_price(ticker = "ETH"):
    while True:
        try:
            r = get(f'https://min-api.cryptocompare.com/data/price?fsym={ticker}&tsyms=USD')
            return r.json()['USD']
        except Exception as e:
            logger.log(f'ERROR | {e}')
            time.sleep(15)


def get_random_amount(_min, _max, digitMin=3, digitMax=5):
    return round(random.uniform(_min, _max), random.randint(digitMin, digitMax))


def wait_balance_is_changed_ETH(
    w3, address, balance_before, wait_time: int = config.BRIDGE_BALANCE_WAIT_TIME, wait_increase: bool = True
):
    waited = 0
    balance_after = balance_before
    if wait_increase:
        logger.info(f"INFO |  Waiting for the ETH bridged onto destination network")
        while balance_after <= balance_before:
            wait_now = random.randint(5, 20)
            sleep(wait_now)
            balance_after = w3.eth.get_balance(address)
            waited += wait_now
            if waited > wait_time:
                logger.error(f"ERROR | There is no any income ETH")
                raise TimeoutError
        return balance_after

def wait_balance_is_changed_token(
        token_contract, address, balance_before, wait_time: int = config.BRIDGE_BALANCE_WAIT_TIME, wait_increase: bool = True
):
    waited = 0
    balance_after = balance_before
    if wait_increase:
        logger.info(f"INFO |  Waiting for the TOKEN bridged onto destination network")
        while balance_after <= balance_before:
            wait_now = random.randint(5, 20)
            sleep(wait_now)
            balance_after = token_contract.functions.balanceOf(address).call()
            waited += wait_now
            if waited > wait_time:
                logger.error(f"ERROR | There is no any income ETH")
                raise TimeoutError
        return balance_after

def wait_balance_after_bridge(wallet_address, dstToken, dstChain, balance_before):
    w3_dst = Web3(Web3.HTTPProvider(dstChain.get("RPC")))
    if dstToken["address"] == config.NATIVE_ADDRESS:
        wait_balance_is_changed_ETH(w3_dst, wallet_address, balance_before)
    else:
        token = w3_dst.eth.contract(
            address=w3_dst.to_checksum_address(dstToken["address"]),
            abi=config.TOKEN_ABI,
        )
        wait_balance_is_changed_token(token, wallet_address, balance_before)
