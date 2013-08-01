#http://community.topcoder.com/stat?c=problem_statement&pm=1694&rd=4580
import os
print os.path.basename(__file__)

#############################

class Point(object):

	def __init__(self, arg):
		super(Point, self).__init__()
		self.arg = arg
		self.X0 = arg[0]	#first coordinate
		self.X1 = arg[1]	#last coordinate
		self.Length = 1 if self.X0 == self.X1 else self.X1 - self.X0 + 1 # Length (diff between coordinate)
		self.Row = arg[2]	#row number in list
		self.ZeroPointX1 = None

	def __add__(self, other):
		if isinstance(other, self.__class__):
			return str(self.Length) + str(other.Length)
		elif isinstance(other, str):
			return str(self.Length) + other
		elif isinstance(other, int):
			return str(self.Length) + str(other)
		else:
			raise TypeError("unsupported operand type(s) for +: '{}' and '{}'").format(self.__class__, type(other))

#############################

def start(value):
	list = []
	X0 = -1

	# create points
	for line in value:
		list_inner = []
		X0 = -1

		for index in range(len(line)):
			# End X
			if X0 != -1 and (line[index] == '-' or (index + 1) == len(line)):
				X1 = index + (1 if (index + 1 == len(line)) and line[index] != '-' else 0)
				list_inner.append(Point([X0, X1, value.index(line) + 1]))
				X0 = - 1
				continue
			# Begin X
			if X0 == -1 and line[index] == 'X':
				X0 = index + 1
				#if end string and last char is X
				if index + 1 == len(line):
					list_inner.append(Point([index + 1, index + 1, value.index(line) + 1]))
					X0 = - 1
			# if only one symbol and it equal '-'
			elif X0 == -1 and line[index] == '-' and len(list_inner) == 0:
				if index + 1 == len(line):
					list_inner.append(Point([0, -1, value.index(line) + 1]))

		if len(list_inner) > 0:
			list.append(list_inner)

	#print list
	# calc 0 situations
	for p1 in reduce(lambda x,y: x + y, list):
		row = p1.Row - 1
		index_curr = list[row].index(p1)
		index_next = index_curr + 1 if (len(list[row]) - 1) > index_curr  else - 1

		curr_X1 = p1.X1
		next_X0 = len(value[row]) + 1 if index_next == -1 else list[row][index_next].X0

		index_prev = list[row].index(p1) - 1 if list[row].index(p1) > 0 else -1

		for p2 in reduce(lambda x,y: x + y, list):
			if p1.Row != p2.Row and p2.X0 > curr_X1 and p2.X1 < next_X0:
				if list[row][index_curr].ZeroPointX1 == None or p2.X0 > list[row][index_curr].ZeroPointX1.X1:
					list[row][index_curr].Length = p1.Length * 10
					list[row][index_curr].ZeroPointX1 = p2

	# if list (more then one value) do reduce (watch overloading) else simple str(Length)
	print [int(reduce(lambda x, y: x + str(y.Length), line) if len(line) > 1 else str(line[0].Length)) for line in list]

#############################

list = ['-------X--------',
        '--XXX----XXXX---',
        '--------------XX']
# #	    { 100,  3040,  2 }
start(list)

list = ["-XXXXXXX--XX-----XXXXX---",
		"---XX----XXX-----XXXX----",
  		"-XXXXX---XXXXX--XXXXXXXX-"]
#		{ 725,  234,  558 }
start(list)

list = ['-XXX---XX----X',
 		'--X----X-XXXXX',
 		'-XX--XXXX---XX'
 		]
#		{ 321,  115,  242 }
start(list)

list = ["--XXX-XXXXXXXX----------XXXXXXXXX--XXXXXXXX-",
  		"--XX----XXXX-----XXXXXX---XXX------XXXXXXXX-",
  		"--------------------X----XXXXXXXX--XXXXXXXX-",
  		"--XX-------X------XXXX----XXX-------XXXXXX--",
  		"--XXX---XXXXX-------X------XX--------X------",
  		"-XXXX--XXXXXXX-----------XXXXXXX----XXXXX---",
  		"-----------X---XXXXXXXX----XX--------XXX----",
  		"-----------X---XXXXXXXX----X----------------",
  		"---X--XXXXXXXX--XXXXXXX---XXX---------------",
  		"--XX---XXXXXXX--XXXXXXX----XX-------XXXXX---" ]
# { 38098,  24638,  188,  21436,  35121,  47075,  1823,  1810,  18730,  27725 }
start(list)

list = ["X","-"]
# { 1,  0 }
start(list)