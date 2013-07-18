import os
print os.path.basename(__file__)

a = 5
suma = 0
mult = 1

while (a > 0):
	suma = suma + (a % 10)  
	mult = mult * (a % 10)
	a = a // 10
	print 'suma: %s' % suma
	print 'mult: %s' % mult
	print a


print 'suma: %s' % suma
print 'mult: %s' % mult
print a
