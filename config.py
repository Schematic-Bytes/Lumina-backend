import logging


class AppConfig:
    PORT = 5000
    MODEL_FILE = "data/yolov8x.pt"


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(process)d] [%(levelname)s] %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
    datefmt="[%Y-%m-%d %H:%M:%S %z]",
    force=True,
)
