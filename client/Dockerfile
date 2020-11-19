FROM python:3.8

RUN mkdir -p /client

WORKDIR /client

ADD . /client

VOLUME ["/client"]

COPY client/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "client/client.py" ]
