#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import sys
import time

from backupMySQL import backup

__AUTHER__ = 'hypo.chen@daocloud.io'

"""
一个可以放在后台执行的死循环，
每执行一次便会SLEEP一天，从而实现每天自动备份数据库，
但是DaoCloud的胶囊主机如果长时间不访问会挂起，因此这个并不适用
"""

if __name__ == '__main__':
    SLEEPTIME = 60 * 60 * 24

    reload(sys)
    sys.setdefaultencoding('utf-8')

    # 我最后还是选择了死循环 TAT
    while True:
        print "Start : %s" % time.ctime()
        backup()
        time.sleep(SLEEPTIME)
        print "End : %s" % time.ctime()
