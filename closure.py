# Closure Property in Python

def makeAdder(addend):
    def adder(augend):
        return augend + addend
    return adder


#>>> a23 = closure.makeAdder(23)   #a23 is a function 
#>>> a23(100)
