#!/usr/bin/python
# File: Basic Class and Property attribute in Python 


class classProperty(object):
    def __init__(self, value):
        self.value = value
        
    def getter(self):
        return self.value

    def setter(self, value):
        self.value = value

    name = property(getter, setter)   #Property attributes




def main():
    """ Highlighting the Property attribute of Python """

    inst = classProperty(10)
    print inst.name

    inst.name = 23
    print inst.name



if __name__=='__main__':
    main()
