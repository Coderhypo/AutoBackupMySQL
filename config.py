#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import time

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
        "您好，数据库[" + BACKUP_CONFIG['DATABASE_NAME'] + \
        "]于 " + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + \
        " 备份成功!\n==============================\n" + \
        "> 备份路径: " + BACKUP_CONFIG['BACKUP_DIR'] + "\n" + \
        "> 文件名称: %s\n> 文件大小: %s\n" + \
        "> 昨日备份文件大小: %s\n" + \
        "=============================\n" + "Daocloud"

BACKUP_ERROR_MASSAGE = \
        "您好，数据库[" + BACKUP_CONFIG['DATABASE_NAME'] + \
        "]于 " + time.strftime("%Y-%m-%d %H:%M", time.localtime()) + \
        " 备份失败，请关注!\n==============================\n" + \
        "Daocloud"

