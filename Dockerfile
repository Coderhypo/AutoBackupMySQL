FROM python:2.7.9

MAINTAINER hypo.chen@daocloud.io

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN chmod +x /app/start.sh

CMD ["/bin/bash", "/app/start.sh"]

EXPOSE 80
