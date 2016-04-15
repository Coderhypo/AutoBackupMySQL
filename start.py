#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import sys
import time

from backupMySQL import backup

__AUTHER__ = 'hypo.chen@daocloud.io'

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
