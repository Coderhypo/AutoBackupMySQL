#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import time
import logging 
import logging.handlers

__AUTHER__ = 'hypo.chen@daocloud.io'

BACKUP_CONFIG = {
    'DATABASE_NAME': os.getenv('DATABASE_NAME') or os.getenv('MYSQL_INSTANCE_NAME') or '',
    'HOST': os.getenv('HOST') or os.getenv('MYSQL_PORT_3306_TCP_ADDR') or 'localhost',
    'USERNAME': os.getenv('USERNAME') or os.getenv('MYSQL_USERNAME') or '',
    'PASSWORD': os.getenv('PASSWORD') or os.getenv('MYSQL_PASSWORD') or '',
    'PORT': os.getenv('PORT') or os.getenv('MYSQL_PORT_3306_TCP_PORT') or '3306',
    'BACKUP_DIR': os.getenv('BACKUP_DIR') or '/backup',
}

EMAIL_CONFIG = {
    'TO': os.getenv('TO') or '',
    'FROM': os.getenv('FROM') or '',
    'PASSWORD': os.getenv('EMAIL_PASSWORD') or '',
    'SMTP': os.getenv('SMTP') or ''
}

BACKUP_SUCCESS_MESSAGE = \
        u"Hello, the database[" + BACKUP_CONFIG['DATABASE_NAME'] + \
        u"] backuped success on " + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + \
        u"\n==============================\n" + \
        u"> path: " + BACKUP_CONFIG['BACKUP_DIR'] + "\n" + \
        u"> filename: %s\n> size: %s\n" + \
        u"> last backup size: %s\n" + \
        u"=============================\n" + u"Daocloud"

BACKUP_ERROR_MASSAGE = \
        u"Hello ,database[" + BACKUP_CONFIG['DATABASE_NAME'] + \
        u"] backup fail on " + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + \
        u" Please pay attention\n==============================\n" + \
        u"Daocloud"

LOG_FILE = 'backup.log'

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler   
fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'  

formatter = logging.Formatter(fmt)   # 实例化formatter  
handler.setFormatter(formatter)      # 为handler添加formatter  
logger = logging.getLogger('backup')    # 获取名为tst的logger  
logger.addHandler(handler)           # 为logger添加handler  
logger.setLevel(logging.DEBUG)

