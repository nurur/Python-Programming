#!/usr/bin/python -tt
# Python Class and Attribute Hiding 

"""
Reference: http://www.tutorialspoint.com/python/

An object's attributes may or may not be visible outside the class 
definition. For these cases, one can name the attributes with a double 
underscore prefix, and those attributes will not be directly visible 
from outside the class. To access such attributes type :
"object._className__attrName"
"""


class simpleCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount


def main():
    counter = simpleCounter()
    counter.count()
    counter.count()
    print "       "
    #print counter.__secretCount  # Attibute Error! 
    print 'Accessing the attribute ouside the class:'
    print counter._simpleCounter__secretCount


if __name__== '__main__':
    main() 
