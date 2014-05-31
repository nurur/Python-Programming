#!/usr/bin/python
# File: Python Class and Attribute Hiding 

''' 
http://www.tutorialspoint.com/python/
An object's attributes may or may not be visible outside the class 
definition. For these cases, one can name the attributes with a double 
underscore prefix, and those attributes will not be directly visible 
from outside the class.
To access such attributes type as "object._className__attrName"
'''


class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount


      
def main():
    counter = JustCounter()
    counter.count()
    counter.count()
    #print counter.__secretCount  # Attibute Error! 
    print counter._JustCounter__secretCount


if __name__== '__main__':
    main() 
