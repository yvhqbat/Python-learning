#!/usr/bin/python

import smtplib
from email.mime.text import MIMEText

sender='liudongwho@126.com'
receiver='yvhqbat@126.com'
subject='python email test'
smtpserver='smtp.126.com'
username='liudongwho@126.com'
password='***'

msg=MIMEText('this is a test email')
msg['Subject']=subject
msg['From']=sender
msg['To']=receiver

smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()


