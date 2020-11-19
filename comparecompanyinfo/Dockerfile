FROM python:3.8

RUN mkdir -p /comparecompanyinfo

WORKDIR /comparecompanyinfo

ADD . /comparecompanyinfo

VOLUME ["/comparecompanyinfo"]

COPY comparecompanyinfo/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "comparecompanyinfo/server.py" ]
