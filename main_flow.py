import pathlib

from app.runner import Runner

if __name__ == "__main__":
    path = pathlib.Path().resolve()
    path = path.joinpath("wallets.txt")
    wallets_path = path.as_posix()
    runner = Runner(wallets_path)
    runner.do_work()
