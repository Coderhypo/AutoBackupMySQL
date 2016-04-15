FROM python:2.7.9

MAINTAINER hypo.chen@daocloud.io

RUN mkdir /app
WORKDIR /app
COPY . /app

ADD crontab /etc/cron.d/backup-mysql
RUN chmod 0644 /etc/cron.d/backup-mysql

CMD cron && tail -f /var/log/cron.log

EXPOSE 80
