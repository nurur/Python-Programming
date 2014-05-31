#!/usr/bin/python
# File: Basic Class in Python 



class eg(object):
    cla = []                     # class atribute
    def __int__(self):           # class initializer 
        self.ins = {}            # instance attribute
  
    def meth1(self,x):           # instance method 
        self.cla.append(x)

    def meth2(self, y, z):       # instance method 
        self.ins[y] = z




def main():
    es1 = python101_class.eg()
    es2 = python101_class.eg()
    es1.cla, es2.cla, es1.ins, es2.ins
    es1.meth1(1); es1.meth2(2,3)
    es2.meth1(4); es2.meth2(5,6)



if __name__== '__main__':
    main() 
