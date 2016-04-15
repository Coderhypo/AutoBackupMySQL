FROM python:2.7.9

MAINTAINER hypo.chen@daocloud.io

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install mysql-client -y

CMD ["python", "/app/start.py"]

EXPOSE 80
