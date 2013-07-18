import os

print os.path.basename(__file__)

x = int(input("enter number: "))
n = ""

print x

while x > 0:
	y = str(x % 2)
	n = y + n
	x = int(x / 2)

	print 'y:%s, n:%s, x:%s' % (y,n,x)

print 'result %s' % n