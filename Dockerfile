FROM ubuntu:trusty
# Ubuntu 14.04, Trusty Tahr(可靠的塔尔羊)发行版

# 道客船长荣誉出品
MAINTAINER Captain Dao (support@daocloud.io)

RUN mkdir /backup
WORKDIR /backup
COPY . /backup

RUN chmod +x backupmysql.sh

CMD ["/bin/bash", "backupmysql.sh"]

EXPOSE 80
