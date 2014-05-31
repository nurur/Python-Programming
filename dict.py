#!/usr/bin/python
# File: Creating dictionary in Python 



def fruitfunc():
    print "I'm a fruit."

def vegetablefunc():
    print "I'm a vegetable."


lookup = {'fruit': fruitfunc, 'vegetable': vegetablefunc}
lookup['fruit']
lookup['vegetable']


print '-' * 30

#test for the existence of a key 
if lookup.has_key('fruit'):
    print 'contains key "fruit"'
  
if 'fruit' in lookup:
    print 'contains key "fruit"'


print '-' * 30

#access the value of a key 
for key in lookup:
    print 'key: %s' %key
    lookup[key]()
