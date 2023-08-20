pip install -r requirements.txt

FILENAME=data/yolov8x.pt
DOWNLOAD_URL=https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x.pt

apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


if [ -f $FILENAME ]; then 
    echo "Model file already exists, skip download.";
else 
    echo "Model file is not found downloading...";
    mkdir "data";
    pushd "data";
        wget $DOWNLOAD_URL;
    popd;
fi

uvicorn app:app --host 0.0.0.0 --port 5000