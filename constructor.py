# Constructor constructs the values of data members of the class.


class MyDict(dict):
    def show(self):
        print 'Showing example for Python 2.7 ...'
        for key in self.keys():
            print 'key: %s  value: %s' % (key, self[key])


def test():
    d = MyDict(one=11, two=22, three=33)
    d.show()
    test()
