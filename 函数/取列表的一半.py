def list_half(x):
	if isinstance(x,list) == True:
		T = []
		for n in range(0,len(x)):
			if n < len(x)/2:
				T.append(x[n])
			else:
				pass
		return T
	else:
		return 'that is not a list,please input again'

a = 1
b = [1,3,4,5,6,3,2]
print list_half(b)
print list_half(a)