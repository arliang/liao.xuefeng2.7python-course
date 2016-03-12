import os
import sys
with open('./bbbb.txt','w') as a:
	a.write('test file')

if 'test' in './bbbb.txt':
	print 'True'

with open('./b/test.txt','w') as b:
	b.write('test file')

c = [x for x in os.listdir('.') if os.path.isfile(x)]
print c