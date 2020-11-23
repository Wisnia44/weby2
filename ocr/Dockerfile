# set base image (host OS)
FROM python:3.8

RUN mkdir -p /ocr
WORKDIR /ocr
ADD . /ocr

VOLUME ["/ocr"]

COPY ocr/requirements.txt .

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y poppler-utils

RUN pip install -r requirements.txt

CMD [ "python", "ocr/ocr.py" ]
