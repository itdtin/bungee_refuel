# Refuel
## Developed by [BenderRoyman](https://t.me/BenderRoyman)

## Prerequisites:
  1. Python 3.10+
  2. wallets.txt in the root with primary keys line by line

## Install
  Be sure that the "python" command runs python 3.10
  1. Create virtual environment: python -m venv venv
  2. Activate venv: source venv/bin/activate - unix, venv\scripts\activate - windows
  3. Install dependencies: pip install -r requirements.txt

## Configure run:
  ### config.py - there are several parts which you would need to configure:

    - Wait time between wallets:
      WAIT_BTW_WALLET_MIN: int = 20
      WAIT_BTW_WALLET_MAX: int = 30
      Final wait time between wallets will be random amount in seconds in range from WAIT_BTW_WALLET_MIN to WAIT_BTW_WALLET_MAX

    - Wait time between run scripts bridge or swap:
      WAIT_BTW_PROJECT_MIN: int = 30
      WAIT_BTW_PROJECT_MAX: int = 40
      Final wait time between run scripts will be random amount in seconds in range from WAIT_BTW_WALLET_MIN to WAIT_BTW_WALLET_MAX

    - Wait time balance on the destination chain:
      WAIT_BALANCE = True - do need to wait balance on the destination chain
      BRIDGE_BALANCE_WAIT_TIME: int = 3600 # 3600 seconds
      Script will wait receiving funds on the destination chain

    Also you need to change RPCs
  ### flows_config.py - there are configs for each flow and you would want to change something, look at the exapmple below:

    PROJECTS = {
      "bungee": [
        {
            "script": "refuel",
            "srcChain": "POLYGON",
            "dstChain": "BSC",
            "amountMin": 1,
            "amountMax": 1.2,
        },
        {
            "script": "refuel",
            "srcChain": "BSC",
            "dstChain": "POLYGON",
            "amountMin": 0.001,
            "amountMax": 0.01,
        },
        ],
      ...
    }

# Run
  python main_flow.py
