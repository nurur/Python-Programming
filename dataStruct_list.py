#!/usr/bin/python -tt

# Data Structure 1
# Creating list in Python 


a=['apple','orange','grape','banana','peach']
b=len(a)-1

for i in a[:b]:
    print i

# Put a seperator between the parts
print '                '


for i in a[:b]:
    tmp = i + '.blah'
    print tmp


print '              '


# append, count, index, insert, pop, remove, reverse, iterate 
items = [111,222,333,444]
print 'list   :', items

items.append(555)
print 'append :', items


print 'count  :', items.count(111)

print 'index  :', items.index(111)


items.insert(0,-111)
print 'insert :', items

print 'pop    :', items.pop()

items.remove(-111)
print 'remove :', items

items.reverse()
print 'reverse:', items 

items.sort()
print 'sort   :', items
print '        '

for item in items:
    print 'item:', item






# End of the script
    
