FROM python:3.8

RUN mkdir -p /checkcompanyinfo

WORKDIR /checkcompanyinfo

ADD . /checkcompanyinfo

VOLUME ["/checkcompanyinfo"]

COPY checkcompanyinfo/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "checkcompanyinfo/server.py" ]
