#!/usr/bin/python -tt
# Closure Property in Python


def makeAdder(addend):
    def adder(augend):
        return augend + addend
    return adder


a23 = makeAdder(23)   #a23 is a function 
print a23(77)
