import logging


class AppConfig:
    PORT = 5000


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
    datefmt="[%Y-%m-%d %H:%M:%S %z]",
    force=True,
)
