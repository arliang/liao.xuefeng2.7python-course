import functools
def log(text):
	if callable(text):
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print 'Begin Call:%s'%text.__name__
			print 'fucntion:%s'%text(*args,**kw)
			return 'End Call:%s'%text.__name__
		return wrapper
	else:
		def d(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print 'Begin Call:%s'%func.__name__
				print 'fucntion:%s'%func(*args,**kw)
				return 'End Call:%s'%func.__name__
			return wrapper
		return d

@log
def f1():
	return '1st..'

@log('guy')
def f2():
	return '2nd..'

print f1()
print f2()
