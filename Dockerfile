FROM ubuntu:trusty
# Ubuntu 14.04, Trusty Tahr(可靠的塔尔羊)发行版

# 道客船长荣誉出品
MAINTAINER Captain Dao (support@daocloud.io)

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN chmod +x /app/backupmysql.sh

CMD ["/bin/bash", "/app/backupmysql.sh"]

EXPOSE 80
