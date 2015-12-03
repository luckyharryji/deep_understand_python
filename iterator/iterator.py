
## define a generator with class
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1
    def __iter__(self):
        return self
    def __repr__(self):
        return '<object with Fab %s>' % self.max
    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()


## define a generator instance with yield
def fab_yield(max):
    n, a, b = 0,0,1
    while n < max:
        yield b
        a , b = b, a+b
        n += 1

## read file with defined buffer
def read_file(f_path):
    Block_Size = 1024
    with open(f_path,'r') as f_in:
        while True:
            content = f_in.read(Block_Size)
            if content:
                yield content
            else:
                return
