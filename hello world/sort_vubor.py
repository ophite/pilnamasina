#http://algolist.manual.ru/sort/select_sort.php
print('sort vubor')
array = [5, 2, 3, 1, 9]

print(array)
print len(array)

temp = 0

n = len(array)

for i in range(0,n):
	min_index = i
	min = array[i]
	
	for j in range(i+1, n):
		if array[j]<min:
			min_index = j
			min = array[j]
	
	array[min_index] = array[i]
	array[i] = min
			
print(array)
print len(array)
