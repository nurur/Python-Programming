# File : Interacting with raw_input


print 'Important Note: '
print 'raw_input() function always takes an input as a string!'

a = raw_input('Input anything you want: string or digit: ')
b = raw_input('Repeat with different values            : ')

print '                               '
print 'Printing inputs as they are ...'
print 'Printing a, b , a+b ...     ...'
print a, b, a+b
print '                               '

print 'Converting inputs using int() function '
print 'Printing int(a), int(b) , int(a)+int(b)'
print int(a), int(b) , int(a)+int(b)
