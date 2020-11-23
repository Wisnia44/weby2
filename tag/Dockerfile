# set base image (host OS)
FROM python:3.8

RUN mkdir -p /tag
WORKDIR /tag
ADD . /tag

VOLUME ["/tag"]
COPY tag/requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python", "tag/tag.py" ]
