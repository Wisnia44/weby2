FROM python:3

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /fontaine

WORKDIR /fontaine

ADD /fontaine /fontaine

VOLUME ["/fontaine"]

#COPY fontaine/manage.py .
#COPY fontaine/requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "manage.py", "makemigrations" ]
CMD [ "python", "manage.py", "migrate"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]

