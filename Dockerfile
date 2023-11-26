FROM python:3.10


ENV PYTHONBUFFERED=1

WORKDIR /code

RUN apt-get update && apt-get install -y libgl1-mesa-glx

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

COPY yolov5l.pt yolov5l.pt

EXPOSE 5100