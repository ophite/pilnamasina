import os
print os.path.basename(__file__)



def sum(*args, **kwargs):
	s = 0

	for x in args:
		if hasattr(x, '__iter__'):
			s = s + sum(*x)
		else:
			s = s + x

	return s



print 'result: %s' % (sum((12,2,10,(3, 3))))