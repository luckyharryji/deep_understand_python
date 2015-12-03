from with_ud import context, with_practice

with with_practice() as f:
    print 'in execution with'


with context() as f_in:
    print 'in execution call'
