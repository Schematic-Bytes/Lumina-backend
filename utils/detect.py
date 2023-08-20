import json
from typing import Optional

from fastapi import UploadFile
from PIL import Image
from ultralytics import YOLO

from config import AppConfig
from utils.runners import run_in_executor

model = YOLO(AppConfig.MODEL_FILE)


@run_in_executor
def detect(image_file: UploadFile) -> Optional[str]:
    with Image.open(image_file.file) as image_buffer:
        data = model.predict(image_buffer)
    first_item = data[0]
    json_data = json.loads(first_item.tojson())
    if len(json_data) == 0:
        return None
    else:
        return json_data[0]["name"]
