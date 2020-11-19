FROM python:3.8

RUN mkdir -p /sendemail

WORKDIR /sendemail

ADD . /sendemail

VOLUME ["/sendemail"]

COPY sendemail/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "sendemail/server.py" ]
