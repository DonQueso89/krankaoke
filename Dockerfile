FROM python:3.8-slim

COPY ./requirements.txt /requirements.txt
RUN apt -y update && apt -y install libpq-dev && pip install -r requirements.txt 

VOLUME /krankaoke_backend
WORKDIR /krankaoke_backend

EXPOSE 8080

CMD ["/usr/local/bin/python", "manage.py", "runserver", "0.0.0.0:8080"]
