#!/usr/bin/python
# File: Python Class 


class Employee:
   """ Common base class for all employees """
 
  # class variable 
   empCount = 0                               

   # class constructor    
   def __init__(self,name,salary):
      print 'Calling Employee Constructor'
      self.name   = name
      self.salary = salary
      Employee.empCount += 1

   # instance method
   def displayCount(self):
      print 'Total Employeed %d'  % Employee.empCount

   # instnace method    
   def displayEmployee(self):
      print 'Name : ', self.name, ', Salary : $', self.salary

   # class destructor
   def __del__(self):
      class_name = self.__class__.__name__
      print class_name, "Class destroyed"




def main():
#Creating instance objects:
   "This would create first object of Employee class"
   emp1 = Employee("Zara", 2000)
   "This would create second object of Employee class"
   emp2 = Employee("Manni", 5000)
   
#Accessing attributes:
   emp1.displayEmployee()
   emp2.displayEmployee()
   print 'Number of employee: %s' %Employee.empCount



if __name__== '__main__':
    main() 
