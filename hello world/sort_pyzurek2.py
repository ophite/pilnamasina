#http://articles.org.ru/docum/sort.php
print('sort pyzurek 2')
array = [5, 2, 3, 11, 22, 9,]

print(array)
print len(array)

n = len(array)

for i in range(0,n):
	for j in range(n-1, i, -1):
		if array[j-1] > array[j]:
			x = array[j-1]
			array[j-1]=array[j]
			array[j]=x

print(array)
print len(array)
