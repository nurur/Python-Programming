# File : Simple example of Nested or Factory function 


def maker(N):
    def action(X):
        return X * N
    return action



def main():
    n = 2
    x = 3
    a = maker(n)(x)
    print 'Inputs are: ', n, x 
    print 'Output from the factory function: %d' %a

if __name__=='__main__':
    main()
