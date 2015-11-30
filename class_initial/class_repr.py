class Point(object):
    """notation for __repr__"""
    def __init__(self, b=0, a=0,c=0):
        self.x = a
        self.y = b
        self.z = c

    def __repr__(self):
        return "Point: X: %s , Y: %s, Z: %s" % (str(self.x),str(self.y),str(self.z))

data = Point(3,8)
print data
