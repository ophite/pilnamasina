import os
print os.path.basename(__file__)

'''
test document info
'''
class Foo(object):
    """docstring for Foo"""

    arg1 = None
    _arg2 = None
    __arg3 = None

    def __init__(self):
        super(Foo, self).__init__()

    def bar(self):
        pass