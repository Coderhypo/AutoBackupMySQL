FROM python:2.7.9

MAINTAINER hypo.chen@daocloud.io

RUN mkdir /app
WORKDIR /app
COPY . /app

CMD ["python", "/app/start.py"]

EXPOSE 80
