#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import os
import datetime

import sendmail
from config import BACKUP_CONFIG
from config import BACKUP_SUCCESS_MESSAGE

__AUTHER__ = 'hypo.chen@daocloud.io'

def check():
    if len(BACKUP_CONFIG['DATABASE_NAME']) == 0:
        return "ERROR: 数据库名缺失！"
    if len(BACKUP_CONFIG['USERNAME']) == 0 or len(BACKUP_CONFIG['PASSWORD']) == 0:
        return "ERROR: 用户名或密码缺失！"

    if BACKUP_CONFIG['BACKUP_DIR'][-1] != '/':
        BACKUP_CONFIG['BACKUP_DIR'] = BACKUP_CONFIG['BACKUP_DIR'] + '/'

    if os.path.exists(BACKUP_CONFIG['BACKUP_DIR']) is False:
        os.makedirs(BACKUP_CONFIG['BACKUP_DIR'])

    return None


def backup():
    
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    print "INFO: 开始执行数据库备份，时间:" + str(today)

    message = check()
    if message:
        print message + '\n'
        sendmail.send("[%s]%s数据库备份失败！" % (today, BACKUP_CONFIG['DATABASE_NAME']))
        print "\nINFO :执行结束， 时间:" + str(today)
        return

    MYSQLDUMP = 'mysqldump --opt -u%s -p%s -h%s %s -P %s | gzip > %s%s.gz' \
            % (BACKUP_CONFIG['USERNAME'], BACKUP_CONFIG['PASSWORD'], BACKUP_CONFIG['HOST'], 
               BACKUP_CONFIG['DATABASE_NAME'],  BACKUP_CONFIG['PORT'], BACKUP_CONFIG['BACKUP_DIR'],str(today))

    try:
        print "INFO: " + MYSQLDUMP
        os.system(MYSQLDUMP)
        print 'INFO: 成功导出数据库'
    except:
        print 'ERROR: 导出数据库失败！\n'
        sendmail.send("[%s]%s数据库备份失败！" % (today, BACKUP_CONFIG['DATABASE_NAME']))
        print "\nINFO :执行结束， 时间:" + str(today)
        return 

    try:
        today_file_size = os.path.getsize('%s%s.gz' % (BACKUP_CONFIG['BACKUP_DIR'], str(today)))
    except:
        today_file_size = 0
    print 'INFO: 今日备份文件大小: ' + str(today_file_size)
    try:
        yesterday_file_size = os.path.getsize('%s%s.gz' % (BACKUP_CONFIG['BACKUP_DIR'], str(yesterday)))
    except:
        yesterday_file_size = 0
    print 'INFO: 查询昨日备份文件大小: ' + str(yesterday_file_size)

    print '\n'
    sendmail.send("[%s]%s数据库备份成功！" % (today, BACKUP_CONFIG['DATABASE_NAME']),
                  BACKUP_SUCCESS_MESSAGE % (BACKUP_CONFIG['BACKUP_DIR'] + str(today), today_file_size, yesterday_file_size))
    print "\nINFO :执行结束， 时间:" + str(today)


if __name__ == '__main__':
    backup()
