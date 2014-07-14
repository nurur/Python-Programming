#!/usr/bin/python -tt

# Data Structure 4
# string formatting is able to use dictionaries to supply the values
# that are inserted. Here is an example:


state='California'
print 'It never rains in sunny %s.' %state

print  '                          '

names = {'tree':'sycamore', 'flower':'poppy', 'herb':'arugula'}
print 'The tree is   : %(tree)s'   %names
print 'The flower is : %(flower)s' %names
print 'The herb is   : %(herb)s'   %names
