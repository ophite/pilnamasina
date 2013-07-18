import os

print os.path.basename(__file__)

a = 122
b = 18

print 'a %d, b %d' % (a, b)

while (a != 0 and b != 0):
	if a > b:
		a = a % b
	else:
		b = b % a

print 'throw divide: %d' % (a + b)

while a != 0 and b != 0:
	if a > b:
		a = a - b
	else:
		b = b - a

print 'throw minus: %d' % (a + b)