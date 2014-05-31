# File : Module & Script (similarities and differences)
#      : Fibonacci numbers module


import sys

def fib1(n):    # write Fibonacci series up to n
    a, b = 0, 1
    print 'Printing Fibonacci series from fib1(n) function ...' 
    while b < n:
        print b,
        a, b = b, a+b


def fib2(n):   # return Fibonacci series up to n
    print 'Printing Fibonacci series from fib2(n) function ...' 
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result



# Main function 
def main():
    print 'Fibonacci series to print'
    inp = int(raw_input('1 from func, 2 from main : '))
    if (inp == 1): 
        fib1( int(sys.argv[1]) )
    else:
        print 'Printing Fibonacci series from main() function'
        print fib2( int(sys.argv[1]) )


if __name__ == '__main__':
    main() 
