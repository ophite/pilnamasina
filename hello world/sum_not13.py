# http://codingbat.com/prob/p167025
import os
print os.path.basename(__file__)

def sum(l):
	print l
	a = lambda x: a(x[:x.index(13)] + x[x.index(13) + 2:]) if (x.count(13) > 0 and x.index(13) + 2 <= len(x)) else (x if x.count(13) == 0 else (x[:x.index(13)]))
	l = a(l)
	print  'result', reduce(lambda res, x: res + (x if x != 13 else 0), l) if len(l) > 0 else 0

# sum([1,2,3,4])
sum([13, 1, 2, 13, 2, 1, 13])
# sum([13, 1, 2])