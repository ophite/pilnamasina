#http://articles.org.ru/docum/sort.php
print('sort pyzurek')
array = [5, 2, 3,]

print(array)
print len(array)

temp = 0
isSorted = False

while isSorted == False:
	i = 0
	isSorted = True
	
	for item in array:
		if i < len(array) - 1 and array[i] > array[i+1]:
			print 'before ' + str(i) + '; i = ' + str(array[i]) + '; i + 1 = ' + str(array[i+1])

			temp = array[i+1]
			array[i+1] = array[i]
			array[i] = temp
			isSorted = False
			
			print 'after ' + str(i) + '; i = ' + str(array[i]) + '; i + 1 = ' + str(array[i+1])
			
		i = i + 1
			
print(array)
print len(array)
