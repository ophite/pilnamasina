print('sort by insert')
array = [3, 9, 2, 5, ]

print(array)
print len(array)

for i in range(0, len(array)):
	temp = array[i]
	j = i - 1
	#print '1array['+str(i)+']='+str(array[i])+'; j='+str(j)
	while temp < array[j]:
		#print '2array['+str(j)+']='+str(array[j]) + '; array['+str(j+1)+']='+str(array[j+1])
		array[j + 1] = array[j]
		j = j - 1
		if j < 0:
			break
	#print '3array['+str(j+1)+']='+str(array[j+1])+'; temp='+str(temp)
	#print array
	array[j + 1] = temp
	#print array

print(array)
print len(array)