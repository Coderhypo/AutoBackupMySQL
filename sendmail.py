#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import smtplib 
from email.mime.text import MIMEText 

from config import EMAIL_CONFIG, BACKUP_ERROR_MASSAGE

__AUTHER__ = 'hypo.chen@daocloud.io'

def check():
    if len(EMAIL_CONFIG['FROM']) == 0 or \
    len(EMAIL_CONFIG['PASSWORD']) == 0 or \
    len(EMAIL_CONFIG['SMTP']) == 0:
        return u"ERROR: SMTP config error!"

    if len(EMAIL_CONFIG['TO']) == 0:
        return u"ERROR: Cant get TO"

    return None

def send(subject, message=BACKUP_ERROR_MASSAGE):

    message = check()

    if message:
        print message
        return 

    print subject
    print message
    
    if _send_mail(subject, message):
        print u'INFO: success send mail to' + EMAIL_CONFIG['TO']
    else:
        print u'ERROR: send mail fail please check EMAIL_CONFIG！'

def _send_mail(subject,content): 
    me = "" + "<" + EMAIL_CONFIG['FROM'] + ">" 
    msg = MIMEText(content) 
    msg['Subject'] = subject 
    msg['From'] = me 
    msg['to'] = EMAIL_CONFIG['TO'] 

    try: 
        s = smtplib.SMTP() 
        s.connect(EMAIL_CONFIG['SMTP']) 
        s.login(EMAIL_CONFIG['FROM'], EMAIL_CONFIG['PASSWORD']) 
        s.sendmail(me, EMAIL_CONFIG['TO'], msg.as_string()) 
        s.close() 
        return True 
    except Exception,e: 
        print str(e) 
        return False 
