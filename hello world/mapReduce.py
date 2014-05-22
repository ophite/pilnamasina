def iter_group(queue):
    buf = []
    prev_key = None
 
    for val in queue:
        cur_key, cur_val = val
        # print 'cur_key',cur_key, 'cur_val',cur_val, 'val', val
        if cur_key == prev_key or prev_key is None:
            buf.append(cur_val)
        else:
            yield prev_key, buf
            buf = []
            buf.append(cur_val)
        prev_key = cur_key
 
    if buf:
        yield cur_key, buf
 
class MapReduce:
    def __init__(self):
        self.queue = []
 
    def send(self, a,b):
        self.queue.append((a,b))
 
    def count(self):
        return len(self.queue)    
 
    def __iter__(self):
        return iter_group(sorted(self.queue))
 
x = MapReduce()
for word in "foo bar bar bar".split():
    x.send(word, 1)
 
for word, ones in x:
    print word, sum(ones)


def power2(start):
	print 'start'
	for i in xrange(start,start+5):
		yield i*i
	print 'finish'


print [i for i in power2(5)]
# def check_Y(items):
# 	for i in items:
# 		if i > 10:
# 			yield i

# a = check_Y([1,21,4,54]) 
# print dir(a)
# print a.__iter__().__reduce__()
