
class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z    
    def __sub__(self, no):
        x = no.x - self.x
        y = no.y - self.y
        z = no.z - self.z
        res = Points(x,y,z)
        return res
    def dot(self, no):
        a = (self.x * no.x)
        b = (self.y * no.y)
        c = (self.z * no.z)
        return a+b+c
    def cross(self, no):
        x = (self.y*no.z)-(self.z*no.y)
        y = (self.z*no.x)-(self.x*no.z)
        z = (self.x*no.y)-(self.y*no.x)
        res = Points(x,y,z)
        return res
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5) #길이

