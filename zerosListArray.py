# File :  Creates a list of n zeros
#      :  Creates an array of n zeros


import sys

def zeroList(n):
    listOfZeros = [0] * n
    return listOfZeros


def zeroArray(n):
    from numpy import zeros
    arrayOfZeros = zeros(n)    
    return arrayOfZeros


def main():
    print 'What would you need : List or Array?'
    inp = int(raw_input('1 for List or 2 for Array : '))
    if (inp == 1):
        zL = zeroList( int(sys.argv[1]) )
        print zL 
    else:
        zA = zeroArray( int(sys.argv[1]) )
        print zA 

        
        
if __name__ == '__main__':
    main()
