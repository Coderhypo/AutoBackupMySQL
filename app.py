#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals
import time
import thread
from flask import Flask

from backupMySQL import backup

__AUTHER__ = 'hypo.chen@daocloud.io'

"""
因为DaoCloud的胶囊长时间没有访问就会挂起，导致自动备份进程结束
受Greenmoon55启发，写了一个访问该容器就能触发备份的WEB
然后把该容器的URL托管在DNSPOD的网站监控里，
DNSPOD会定期访问该网站，检查该网站是否挂掉
因此触发了数据库备份功能，我脑洞真大
"""

app = Flask(__name__)

LASTTIME = None
MINTIME = 60 * 60 * 2 # 最少间隔2小时

@app.route('/')
def start_backup():
    global LASTTIME
    if LASTTIME is None or time.time() - LASTTIME > MINTIME:
        thread.start_new_thread(backup, ())
        LASTTIME = time.time()
        
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
