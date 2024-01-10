import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def ConsoleInfo(msg: str):
    return logging.info(msg)
