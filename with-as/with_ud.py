from __future__ import with_statement
from contextlib import contextmanager

class with_practice:
    def __enter__(self):
        print "in enter"
    def __exit__(self,e_t,e_v,t_b):
        print 'in exit'


@contextmanager
def context():
    print 'enter defination'
    try:
        yield
    except Exception,e:
        raise e
    else:
        print 'with no error'
