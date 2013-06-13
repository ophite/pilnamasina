#http://ru.wikipedia.org/wiki/%D0%9D%D0%B0%D0%B8%D0%B1%D0%BE%D0%BB%D1%8C%D1%88%D0%B0%D1%8F_%D0%BE%D0%B1%D1%89%D0%B0%D1%8F_%D0%BF%D0%BE%D0%B4%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B0
print('find similar substrings')
string_x = 'SUBSEQUENCE'
string_y = 'SUBEUENCS'

print string_x + ' x(%s)' % (len(string_x))
print string_y + '   y(%s)' % (len(string_y))

'''11x9
  SUBSEQUENCE
  000000000000
S 010010000000
U 002000010000
B 000300000000
E 000001001001
U 001000010000
E 000001002001
N 000000000300
C 000000000040
S 010010000000
'''

#############################

def printArray(arr):

	print ''
	line = ''
	word = ''
	for y in range(len(string_y)):
		line = ''
		word = ''
		for x in range(len(string_x)):
			try:
				if y == 0:
					word = ('  ' if x == 0 and y == 0 else '') + word + string_x[x] + ' '

				if x == 0:
					line = line + string_y[y] + ' '

				line = line + str(arr[y][x]) + ' '
			except Exception as ex:
				print 'error: ', x, y, ex

		print (word + '\n' if len(word) > 0 else '') + line

#############################

def start():
	array = [[0 for x in range(len(string_x))] for y in range(len(string_y))]

	# before
	printArray(array)
	max_x = 0
	max_y = 0
	max = 0

	for y in range(len(string_y)):
		for x in range(len(string_x)):
			if string_y[y]==string_x[x]:
				array[y][x] = 1

			if y == 1 or x == 1:
				continue

			if string_y[y]==string_x[x]:
				array[y][x] = array[y-1][x-1] + 1

			if array[y][x] > max:
				max_y = y
				max_x = x
				max = array[y][x]

	# after
	printArray(array)

	print ''
	#print max,max_y,max_x
	print string_y[max_x - max - 1:max_x - 1]

#############################
start()