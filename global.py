#
NAME = 'Peach'

def show_global():
    name = NAME
    print '(show_global) name: %s' %name


def set_global():
    NAME = 'Nectarine'
    name = NAME
    print '(set_global) name : %s' %name


show_global()
set_global()
show_global()
#
#
print '                          '
#
#
def set_global():
    global NAME
    NAME = 'Nectarine'
    name = NAME
    print '(set_global) name: %s' % name

show_global()
set_global()
show_global()
