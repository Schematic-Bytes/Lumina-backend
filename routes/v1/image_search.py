from fastapi import UploadFile, status
from fastapi.responses import JSONResponse

from utils.detect import detect


async def image_reverse_lookup(file: UploadFile):
    label_name = await detect(file)
    if label_name is None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "could not detect object."})
    return {"label": label_name}
