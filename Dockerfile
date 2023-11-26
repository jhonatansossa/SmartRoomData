FROM python:3.10


ENV PYTHONBUFFERED=1

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . . 

COPY yolov5l.pt yolov5l.pt

EXPOSE 5100