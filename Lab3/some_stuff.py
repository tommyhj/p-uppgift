from functools import reduce

def sum(a,b):
	return reduce((lambda x,y: x+y), range(a,(b+1)))

print (str(sum(1,100)))