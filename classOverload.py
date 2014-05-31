#!/usr/bin/python
# File : Python Class and Operator overloading 


class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "destroyed"

   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

   def __sub__(self,other):
      return Vector(self.a - other.a, self.b - other.b)

   def __mul__(self,other):
      return Vector(self.a * other.a, self.b * other.b)

   def __div__(self,other):
      return Vector(self.a / other.a, self.b / other.b)



'''
v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2; print v1-v2
print v1*v2; print v1/v2
'''
