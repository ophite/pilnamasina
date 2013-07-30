import os
print os.path.basename(__file__)

a = int(input("value: "))

print 'a = %d' % a

fact = lambda f: 1 if f == 0 else f * fact(f-1)

print 'result: %d' % fact(a)