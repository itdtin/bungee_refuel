import pathlib

from app.runner import Runner

if __name__ == "__main__":
    path = pathlib.Path().resolve()
    wallets_path = "wallets.txt"
    runner = Runner(wallets_path)
    runner.do_work()
