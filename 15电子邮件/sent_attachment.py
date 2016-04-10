# -*- coding:utf-8 -*-
import smtplib
import string
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


def _format_addr(s):
	name,addr = parseaddr(s)
	return formataddr((\
		Header(name,'utf-8').encode(),\
		addr.encode('utf-8') if isinstance(addr,unicode) else addr))

from_addr = 'moon.qiu@int-fly.com'
password = 'shanbeck'
smtp_server = 'mail.int-fly.com'
to_addr = ('moon.qiu@int-fly.com,moon.qiu198909@hotmail.com')
#to_addr = ('460384737@qq.com,vitionst@qq.com,15013912999@qq.com,375235513@qq.com')
to_addr = string.splitfields(to_addr,',')
#邮件对象：
msg = MIMEMultipart()
msg['From'] = _format_addr(u'管理员<%s>'%from_addr)
msg['TO'] = _format_addr(u'<%s>'% (to_addr))
msg['Subject'] = Header(u'来自轩然大叔的测试邮件。。。','utf-8').encode()

#邮件正文是 MIMEText：
##msg.attach(MIMEText('send with file...','plain','utf-8'))
#附件图片 通过cid：x的方式在正文中显示图片
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
					'<p><img src="cid:0"></p>' +
					'</body></html>','html','utf-8'))

#添加附件 MIMEBase
with open('./test.jpg','rb') as f:
	mime = MIMEBase('image','png',filename = 'test.jpg')
	mime.add_header('content-Disposition','attachment',filename='test.jpg')
	mime.add_header('content-id','<0>')
	mime.add_header('X-Attachement-Id','0')
	mime.set_payload(f.read())
	encoders.encode_base64(mime)
	msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
try:
	server.login(from_addr,password)
	print "login success"
except:
	print 'login fail'

try:
	server.sendmail(from_addr,to_addr,msg.as_string())
	print 'send success'
except:
	print 'send fail'

server.quit()
'''
server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()
'''