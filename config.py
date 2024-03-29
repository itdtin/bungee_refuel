import dotenv
from app.helpers.abis import REFUEL_ABI

dotenv.load_dotenv()

to_random_run = ["bungee"]

# Wait
WAIT_BTW_WALLET_MIN: int = 20
WAIT_BTW_WALLET_MAX: int = 30

WAIT_BTW_PROJECT_MIN: int = 30
WAIT_BTW_PROJECT_MAX: int = 40

WAIT_RECEIPT = [(4,5), (7,8)]

WAIT_BALANCE = True
BRIDGE_BALANCE_WAIT_TIME = 3600 # 3600 seconds

ATTEMTS_TO_NODE_REQUEST = 9
ATTEMTS_TO_API_REQUEST = 9

NATIVE_DECIMALS: str = "ether"
NATIVE_ADDRESS: str = "0x0000000000000000000000000000000000000000"

#Bungee addresses
REFUEL_ARBITRUM: str = "0xc0e02aa55d10e38855e13b64a8e1387a04681a00"
REFUEL_OPTIMISM: str = "0x5800249621DA520aDFdCa16da20d8A5Fc0f814d8"
REFUEL_POLYGON: str = "0xAC313d7491910516E06FBfC2A0b5BB49bb072D91"
REFUEL_AVALANCHE: str = "0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB"
REFUEL_BSC: str = "0xBE51D38547992293c89CC589105784ab60b004A9"
REFUEL_FANTOM: str = "0x040993fbF458b95871Cd2D73Ee2E09F4AF6d56bB"

# Networks
ARBITRUM_RPC: str = "https://arb-mainnet.g.alchemy.com/v2/aFjqA3mR0fMDkPR8lMF2QnjNQPNi9Jcm"
ARBITRUM_CHAIN_ID: int = 42161

OPTIMISM_RPC: str = "https://opt-mainnet.g.alchemy.com/v2/0K6bMED4RlCn2DPr8tKQS8XTRMcUDKFR"
OPTIMISM_CHAIN_ID: int = 10

POLYGON_RPC: str = "https://polygon-mainnet.g.alchemy.com/v2/ncSSy-j4i1T3hcN5hFCtEsyghpLCw_0p"
POLYGON_CHAIN_ID: int = 137

AVALANCHE_RPC: str = "https://avalanche-mainnet.infura.io/v3/ca0d7f3c70f84e22ab29e5a74b329a3a"
AVALNCHE_CHAIN_ID: int = 43114

BSC_RPC: str = "https://bsc-dataseed4.binance.org"
BSC_CHAIN_ID: int = 56

FANTOM_RPC: str = "https://rpc.ankr.com/fantom"
FANTOM_CHAIN_ID: int = 250


NETWORKS = {
    "ARBITRUM": {
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": ARBITRUM_CHAIN_ID,
        "RPC": ARBITRUM_RPC,
        "REFUEL_ADDRESS": REFUEL_ARBITRUM,
    },
    "POLYGON": {
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": POLYGON_CHAIN_ID,
        "RPC": POLYGON_RPC,
        "REFUEL_ADDRESS": REFUEL_POLYGON,
    },
    "OPTIMISM": {
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": OPTIMISM_CHAIN_ID,
        "RPC": OPTIMISM_RPC,
        "REFUEL_ADDRESS": REFUEL_OPTIMISM,
    },
    "BSC": {
        "GAS_MULTIPLIER": 3,
        "CHAIN_ID": BSC_CHAIN_ID,
        "RPC": BSC_RPC,
        "REFUEL_ADDRESS": REFUEL_BSC,
    },
    "AVALANCHE": {
        "GAS_MULTIPLIER": 5,
        "CHAIN_ID": AVALNCHE_CHAIN_ID,
        "RPC": AVALANCHE_RPC,
        "REFUEL_ADDRESS": REFUEL_AVALANCHE,
    },
    "FANTOM": {
        "GAS_MULTIPLIER": 6,
        "CHAIN_ID": FANTOM_CHAIN_ID,
        "RPC": FANTOM_RPC,
        "REFUEL_ADDRESS": REFUEL_FANTOM,
    },
}
