# File : python101_module1.py

"""
This simple module contains definitions of a class and several functions.
"""

print
LABEL = '===== Testing a simple module ====='

class Person:
    """A simple class definition.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def show(self):
        print 'Person -- name:%s  description:%s' %(self.name,self.description)


def test(msg, count):
    """A simple function.
    """
    for idx in range(count):
        print '%s %d' % (msg, idx)


def testDefaultArgs(arg1='default1', arg2='default2'):
    """A function with default arguments.
    """
    print 'arg1:', arg1
    print 'arg2:', arg2


def testArgLists(*args, **kwargs):
    """
    A function which references the argument list and keyword arguments.
    """
    print 'args:', args
    print 'kwargs:', kwargs


def main():
    """
    A test harness for this module.
    """
    
    print LABEL
    print
    
    person = Person('Herman', 'A cute guy')
    person.show()
    print '=' * 30
    
    test('Test #', 4)
    print '=' * 30

    testDefaultArgs('Explicit value')
    print '=' * 30
    testArgLists('aaa', 'bbb', arg1='ccc', arg2='ddd')

if __name__ == '__main__':
    main()
