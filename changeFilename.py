# Read file name from the current directory 
# use os module
from os import listdir
from os.path import isfile, join
fileName1 = [ f for f in listdir(".") if isfile( join(".",f) ) ]
print fileName1
print ' '
# use glob module  
import glob
fileName2 = glob.glob("./*")  # without "./" use glob.glob("*") 
print fileName2



# Change file names recursively 
import os
for filename in os.listdir("."):
    if filename.startswith("python_"):
        os.rename(filename, filename[7:])

