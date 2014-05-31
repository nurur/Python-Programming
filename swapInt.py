# File: Swap two integers
#     : Returns a tuples of length 2 


def swapTmp(a, b):
    t = a
    a = b
    b = t 
    return (a, b)


def swapXor(a, b):
    b = a^b
    a = a^b
    b = a^b 
    return (a, b)
