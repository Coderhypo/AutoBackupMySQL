#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import datetime

import sendmail
from config import logger
from config import BACKUP_CONFIG
from config import BACKUP_SUCCESS_MESSAGE

__AUTHER__ = 'hypo.chen@daocloud.io'

def check():
    if len(BACKUP_CONFIG['DATABASE_NAME']) == 0:
        return u"ERROR: Cant get DATABASE_NAME!"
    if len(BACKUP_CONFIG['USERNAME']) == 0 or len(BACKUP_CONFIG['PASSWORD']) == 0:
        return u"ERROR: Cant get USERNAME or PASSWORD!"

    if BACKUP_CONFIG['BACKUP_DIR'][-1] != '/':
        BACKUP_CONFIG['BACKUP_DIR'] = BACKUP_CONFIG['BACKUP_DIR'] + '/'

    if os.path.exists(BACKUP_CONFIG['BACKUP_DIR']) is False:
        os.makedirs(BACKUP_CONFIG['BACKUP_DIR'])

    return None


def backup():
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    logger.info(u"Start Backup! time:" + str(today))

    message = check()
    if message:
        logger.debug(message)
        sendmail.send(u"[%s]%s Backup fail!" % (today, BACKUP_CONFIG['DATABASE_NAME']))
        logger.info(u"end time:" + str(today))
        return

    MYSQLDUMP = 'mysqldump --opt -u%s -p%s -h%s %s -P %s | gzip > %s%s.gz' \
            % (BACKUP_CONFIG['USERNAME'], BACKUP_CONFIG['PASSWORD'], BACKUP_CONFIG['HOST'], 
               BACKUP_CONFIG['DATABASE_NAME'],  BACKUP_CONFIG['PORT'], BACKUP_CONFIG['BACKUP_DIR'],str(today))

    try:
        logger.debug(MYSQLDUMP)
        os.system(MYSQLDUMP)
        logger.info(u'INFO: mysqldump success!')
    except:
        logger.error(u'mysqldump fail')
        sendmail.send(u"[%s]%s Backup fail!" % (today, BACKUP_CONFIG['DATABASE_NAME']))
        logger.info(u"end time:" + str(today))
        return 

    try:
        today_file_size = os.path.getsize('%s%s.gz' % (BACKUP_CONFIG['BACKUP_DIR'], str(today)))
    except:
        today_file_size = 0
    logger.info(u'backup file size(today): ' + str(today_file_size))
    try:
        yesterday_file_size = os.path.getsize('%s%s.gz' % (BACKUP_CONFIG['BACKUP_DIR'], str(yesterday)))
    except:
        yesterday_file_size = 0
    logger.info(u'backup file size(yesterday): ' + str(yesterday_file_size))

    sendmail.send(u"[%s]%s Backup success!" % (today, BACKUP_CONFIG['DATABASE_NAME']),
                  BACKUP_SUCCESS_MESSAGE % (BACKUP_CONFIG['BACKUP_DIR'] + str(today), today_file_size, yesterday_file_size))
    logger.info(u"end time:" + str(today))


if __name__ == '__main__':
    backup()
