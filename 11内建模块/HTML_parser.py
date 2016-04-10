# -*- coding:utf-8 -*-
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from urllib2 import urlopen

class MyHtmlParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		print '<%s>'%tag

	def handle_endtag(self, tag):
		print '</%s>'%tag

	def handle_startendtag(self, tag, attrs):
		print '<%s/>' % tag

	def handle_data(self, data):
		print 'data'

	def handle_comment(self, data):
		print '<!-- -->'

	def handle_entityref(self, name):
		print '&%s;'%name

	def handle_charref(self, name):
		print '&#%s;'%name

parser = MyHtmlParser()
c = '<html><head></head><body><p>Some <a href=\"#\">html</a>tutorial...<br>END</p></body></html>'
b = urlopen("https://www.python.org/events/python-events/").read()
#parser.feed(c)


#content > div > section > div > div > ul > li:nth-child(1) > h3 > ac
L = []
class MyHTMLParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		super(MyHTMLParser, self).__init__()
		self.key = {'time': None, 'event-title': None, 'event-location': None}

	def handle_starttag(self, tag, attrs):
		if tag == 'time':
			self.key['time'] = True
		elif tag == 'span' and attrs.__contains__(('class', 'event-location')):
			self.key['event-location'] = True
		elif tag == 'h3' and attrs.__contains__(('class', 'event-title')):
			self.key['event-title'] = True

	def handle_data(self, data):
		if self.key['time']:
			print  'Time:%s\t|' % data,
			self.key['time'] = None
			L.append('Time:%s\t|' % data)
		elif self.key['event-title']:
			print 'Title:%s\t|' % data,
			self.key['event-title'] = None
			L.append('Title:%s\t|' % data)
		elif self.key['event-location']:
			print 'Location:%s|\n' % data,
			self.key['event-location'] = None
			L.append('Location:%s|\n' % data)

parser = MyHTMLParser()
html = urlopen('http://www.python.org/events/python-events/').read()
parser.feed(html)
d = parser.feed(html)
print parser.feed(html)
print L

with open('./htmlparser.txt','wb') as file_write:
	file_write.write(''.join(L))    #list 转换为str
	file_write.close()

list = ['a','b','c']
print ''.join(list)

