

def enumerator(seq):
    n = 0
    for item in seq:
        yield n, item
        n += 1


def main():
    seq = [9, 2, 7, 4, 6]
    x = enumerator(seq)
    print x



if __name__=='__main__':
    main()
