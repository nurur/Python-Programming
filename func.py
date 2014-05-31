#
# File: Basic functions


# Example 1
# Function with default arguments
print
print 'function with default arguments'
def testDefaultArgs(arg1='default1', arg2='default2'):
    "docstring practice"
    print 'arg1:', arg1
    print 'arg2:', arg2

testDefaultArgs()
#testDefaultArgs('Explicit value')


# Function with 'positional' arguments followed by 'keyword' arguments
#
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "Volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"


parrot(1000)



# Example 2a
# Function with arguments lists(*name) and keyword argument lists(**name)
print
def cheeseshop(kind, *arguments, **keywords):
    print
    print "-- Do you have any", kind, '?'
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
        print '-'*40
        for kw in keywords.keys():
            print kw, ':', keywords[kw]

#
cheeseshop('Limburger', "It's very runny, sir.",
           client='John Cleese',
           shopkeeper='Michael Palin',
           sketch='Cheese Shop Sketch')


# Example 2b
# Function with arguments lists(*name) and keyword argument lists(**name)
print 
def testArgLists_1(*args, **kwargs):
    print 'args:', args
    print 'kwargs:', kwargs
            
testArgLists_1('aaa', 'bbb', arg1='ccc', arg2='ddd')

def testArgLists_2(arg0, *args, **kwargs):
    print 'arg0: "%s"' % arg0
    print 'args:', args
    print 'kwargs:', kwargs
            
print '=' * 40
testArgLists_2('a first argument', 'aaa', 'bbb', arg1='ccc', arg2='ddd')




#Example 3
# Function with generic arguments 
def test(msg, count):
    "docstring practice"
    for idx in range(count):
        print '%s %d' % (msg, idx)
#
print 
test('test #', 4)


print '          '
print 'from tuple'
# Create a tuple:
val = (test, 'A label:', 5)

# Call the function:
val[0](val[1], val[2])




# Example 4
print ' '
print 'function that prints number'
# Write Fibonacci series up to n
def fib1(n):    
    "Print Fibonacci series up to n"
    a, b = 0, 1
    while b < n:
        a, b = b, a+b
        print b,
#
fib1(2000)   #call


print
print "function that returns a 'list' of numbers"
#
def fib2(n): # Return Fibonacci series up to n
    "Return a 'list' containing the Fibonacci series up to n"
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)    
        a, b = b, a+b
        return result
#
fib2(2000)   #call
