# set base image (host OS)
FROM python:3.8

RUN mkdir -p /tax_cal
WORKDIR /tax_cal
ADD . /tax_cal

VOLUME ["/tax_cal"]
COPY tax_cal/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "tax_cal/service.py" ]
