#!/usr/bin/python
# File: Python Class, ClassMethod & StaticMethod 


class Avdanced:
   count = 10 
    
   def __init__(self, name):
       self.name = name
    
   @staticmethod 
   def staticDescription(count, name):
       print 'This is  the staticMethod from advanced class.' 
       print '%s from staticMethod' %name

   #def staticDescription():
   #    return 'This is  the staticMethod from advanced class.' 
   #staticDescription = staticmethod(staticDescription)
 

   @classmethod
   def classDescription(cls,name):
       print 'This is  the classMethod from advanced class.' 
       print '%s from classMethod' %name

   #def classDescription(cls):
   #    print 'This is  the classMethod from advanced class.' 
   #classDescription = classmethod(staticDescription)


       
def main():
    obj = Avdanced('')
    obj.staticDescription(10, 'Zara')
    obj.classDescription('Tom')
    print Avdanced.count


if __name__== '__main__':
    main() 
