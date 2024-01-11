from apache_beam import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s -  %(message)s"
)


def ConsoleInfo(msg: str):
    return logging.info(msg)


def WarningInfo(msg: str):
    logging.basicConfig(
        level=logging.WARNING, format="%(asctime)s - %(levelname)s -  %(message)s"
    )
    return logging.info(msg)
