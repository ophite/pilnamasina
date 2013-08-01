import os
print os.path.basename(__file__)

#############################

def recurs(value, plus_count):
	if len(value) > 1 and plus_count > 0:
		list = [value[:1] + '+' + x for x in recurs(value[1:], plus_count - 1) if x != '']
		return [value[:1]       + x for x in recurs(value[1:], plus_count)     if x != ''] + list
	else:
		return [value]

#############################

def start(string, sum_in):
	d = {}
	for str in reduce(lambda x,y: x + y, [recurs(string, i + 1) for i in range(len(string)-1)]):
		str = str[2:] if str.startswith('0+') else str
		str = str[1:].replace('+0','+') if str.startswith('0') else str.replace('+0','+')
		list = [s for s in str.split('+') if s != '']
		sum = reduce(lambda res, x: res+x, [int(s) for s in list])

		if sum == sum_in:
			d[str] = [sum, len(list) - 1]

	print {str : [sum_in, - 1]} if len(d) == 0 else min(d.items(), key = lambda x: x[1][1])

#############################

start('345', 48)
start('382834', 100)
start('99999', 45)
start('303', 6)
start('0123456789', 45)
start('923056000001', 71)
start('99999', 100)
