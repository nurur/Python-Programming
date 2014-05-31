
# File: Write the list of builtin functions and variables to a file 


# writing string to a file 1
outfile = file('tmpWrite.txt', 'w')
outfile.write('This is line #1\n')
outfile.write('This is line #2\n')
outfile.write('This is line #3\n')
outfile.close()


# writing list to a file 1
import __builtin__
a = dir(__builtin__)

builtin = open('builtin.txt', 'w')

# Case 1:
builtin.writelines("%s\n" %a[i] for i in range(len(a)) )
builtin.close()


"""
# Case 2:
for i in range(len(a)):
    print i+1, ' ', a[i]
    builtin.write("%s\n" %a[i])

builtin.close()
"""



# reading 1
infile = file('tmpWrite.txt', 'r')
for line in infile.readlines():
    print 'Line:', line
infile.close()

# Note
# infile.readlines()" returns a list of lines in the file
# for large files use the file object itself or "infile.xreadlines()",



# reading 2
infile = file('tmpWrite.txt', 'r')
for line in infile:
    print 'Line:', line
