import os
print os.path.basename(__file__)

# bad
def fib(n):
	if n == 1 or n ==2:
		return 1

	sum = fib(n-2) + fib(n-1)

	print n, sum

	return sum 


# good
def fib_new(n):
	print n
	arr = range(n)

	for i in range(n):
		if i == 0:
			arr[i] = 0
		elif i == 1:
			arr[i] = 1
		else: 
			arr[i] = arr[i-2] + arr[i-1]

	print arr
	return {'sum':reduce(lambda x, res: x + res, arr), 'last':arr[n-1]}

#print 'fibonachi: %d' % (fib(6))
print 'fibonachi new: %s' % (fib_new(50))
