import os
print os.path.basename(__file__)

l = [10, 45, 24, 43, 89, 15, 16, 23, 89, 23, 35, 64, 21, 12, 45]

print 'list: %s' % l

def qs(list, first, last):
	print 'list: %s' % list

	mid = list[(int)((first + last) / 2)]
	print 'mid: %s' % mid

	l = first
	r = last

	while l < r:

		while list[l] < mid:
			l = l + 1

		while list[r] > mid:
			r = r - 1

		if l <= r:
			temp = list[l]
			list[l] = list[r]
			list[r] = temp

			l = l + 1
			r = r - 1

	if first < r:
		qs(list, first, r) 

	if last > l:
		qs(list, l, last)

qs(l, 0, len(l) - 1)