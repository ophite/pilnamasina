# coding=utf-8 
#http://younglinux.info/book/export/html/60
import os
print os.path.basename(__file__)

list = [0,3,5,7,10,20,28,30,45,56]

print(list)
print len(list)
search_item = 45
print search_item

def bs(list, first, last, x):
	mid_index = (int)(first + last) / 2
	mid = list[mid_index]
	print 1
	#return 
	
	if mid < x:
		return bs(list, mid_index + 1, last, x)

	if mid > x:
		return bs(list, first, mid_index - 1, x) 

	return mid_index 

def bs2(list, x):
	i = 0
	j = len(list)-1
	m = int(j/2)

	while list[m] != x and i < j:
		print 1

		if x > list[m]:
			i = m+1
		else:
			j = m-1

		m = int((i+j)/2)

	if i > j:
	    print 'cant find'
	else:
	    print 'index: %s' % m

print '----------------'
print 'index: %s' % bs(list, 0, len(list) - 1, search_item)
print '----------------'
bs2(list, search_item)