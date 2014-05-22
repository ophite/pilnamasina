#http://habrahabr.ru/post/145369/

import os
print os.path.basename(__file__)

os.path.basename()

x = 10;

def create_func_plus_constant(n):
	def plusfunc(k):
		return n + k
	return plusfunc

def create_lambda_plus_constant(n):
	return lambda x: x + n

print '---------------------'
f = create_func_plus_constant(9)
print f(5)
print f(11)

print '---------------------'
f2 = create_lambda_plus_constant(19)
print f2(5)
print f2(11)

#########################################
def list_funcs_plus_constant(start, end):
	return [ create_func_plus_constant(i) for i in range(start,end)]

print list_funcs_plus_constant(5, 10)

#########################################
import collections

def funcs_vs_args(func, args):

	print args.__class__
	print args

	if isinstance(func, collections.Iterable):
		return [tuple(map(f, args)) for f in func]
	else:
		return [tuple(map(func, args))]

print '---------------------'
print funcs_vs_args(f, (1,3,5))
print funcs_vs_args([f, f2], (1,3,5))