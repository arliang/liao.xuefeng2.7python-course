# -*- coding:utf-8 -*-
from email.mime.text import MIMEText
import smtplib
msg = MIMEText('hello,send by Python script.','plain','utf-8')

#输入email地址和口令
#from_addr = raw_input('From:')
from_addr = 'moon.qiu@int-fly.com'
#password = raw_input('Password:')
password = 'shanbeck'
#SMTP server
#smtp_server = raw_input('SMTP server:')
smtp_server = 'mail.int-fly.com'
#addressee
#to_addr = raw_input('TO:')
to_addr = 'moon.qiu198909@hotmail.com'

server = smtplib.SMTP(smtp_server,25)#default port number usually is 25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()


