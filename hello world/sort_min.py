print('sort by min value')
array = [9, 2, 5, 3,]

print(array)
print len(array)

i = 0
j = 0
min = 0
pos = 0
temp = 0

n = len(array)

print n

for i in range(0, n-1):
	min = array[i]
	pos = i

	for j in range(i+1, n):
		if array[j] < min:
			min = array[j]
			pos = j
	
	temp = array[i]
	array[i] = array[pos]
	array[pos] = temp
			
print(array)
print len(array)
