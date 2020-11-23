# set base image (host OS)
FROM python:3.8

RUN mkdir -p /Dane_kup
WORKDIR /Dane_kup
ADD . /Dane_kup

VOLUME ["/Dane_kup"]
COPY Dane_kup/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "Dane_kup/service.py" ]
