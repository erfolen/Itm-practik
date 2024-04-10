FROM python:3.11

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN apt-get update && apt-get -y install tesseract-ocr

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh

#COPY . /src
#WORKDIR src

#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000