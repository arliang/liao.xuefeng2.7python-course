# -*- coding:utf-8 -*-

from email import encoders
import string
from email.header import  Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
import smtplib
import re

def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((\
		Header(name,'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr,unicode)else addr))

#from_addr = raw_input('From:')
from_addr = 'moon.qiu@int-fly.com'
#password = raw_input('Password:')
password = 'shanbeck'
#SMTP server
#smtp_server = raw_input('SMTP server:')
smtp_server = 'mail.int-fly.com'
#addressee
#to_addr = raw_input('TO:')
to_addr_1 = ('moon.qiu@int-fly.com,moon.qiu198909@hotmail.com')
to_addr_2 = string.splitfields(to_addr_1,",")
to_addr_3 = re.split(r'[\@\,]',to_addr_1)
'''
#两种方式，一种是将str的to_addr 转化为list类型以，号分割，另外一种是直接以list传入msg['TO']，起到发送多个邮箱的目的
to_addr = ['moon.qiu@int-fly.com', 'moon.qiu198909@hotmail.com']
'''
to_addr_list = [to_addr_3[x] for x in range(0,len(re.split(r'[\@\,]',to_addr_1))) if x % 2 == 0]
#普通文本形式
#msg = MIMEText('hello,send by Python..','plain','utf-8')

#html形式
#msg = MIMEText('<html><body><h1>hello</h1>'+'<p>send by <a href="http://www.python.org">Python</a>...</p>'+'</body></html>','html','utf-8')
#直接打开html文件当文本发送
html_read = open('./python_org.html','rb')
msg = MIMEText(html_read.read(),'html','utf--8')
msg['From'] = _format_addr(u'Python 爱好者<%s>'% from_addr)
msg['TO'] = _format_addr(u'%s<%s>'%(to_addr_list,to_addr_2))
msg['Subject'] = Header(u'来自SMTP的问候。。。','utf-8').encode()


server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr_2,msg.as_string())
server.quit()
