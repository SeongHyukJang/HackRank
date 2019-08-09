class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        x,y = (self.real+no.real),(self.imaginary+no.imaginary)
        if y == 0:
            result = "%.2f+0.00i" % (x)
        elif x == 0:
            if y >= 0:
                result = "0.00+%.2fi" % (y)
            else:
                result = "0.00-%.2fi" % (abs(y))
        elif y > 0:
            result = "%.2f+%.2fi" % (x,y)
        else:
            result = "%.2f-%.2fi" % (x, abs(y))
        return result        
    def __sub__(self, no):
        x,y = self.real-no.real,self.imaginary-no.imaginary
        if y == 0:
            result = "%.2f+0.00i" % (x)
        elif x == 0:
            if y >= 0:
                result = "0.00+%.2fi" % (y)
            else:
                result = "0.00-%.2fi" % (abs(y))
        elif y > 0:
            result = "%.2f+%.2fi" % (x,y)
        else:
            result = "%.2f-%.2fi" % (x, abs(y))
        return result
    def __mul__(self, no):
        num = complex(self.real,self.imaginary) * complex(no.real,no.imaginary)
        x,y = num.real,num.imag
        if y == 0:
            result = "%.2f+0.00i" % (x)
        elif x == 0:
            if y >= 0:
                result = "0.00+%.2fi" % (y)
            else:
                result = "0.00-%.2fi" % (abs(y))
        elif y > 0:
            result = "%.2f+%.2fi" % (x,y)
        else:
            result = "%.2f-%.2fi" % (x, abs(y))
        return result
    def __truediv__(self, no): 
        num = complex(self.real,self.imaginary) / complex(no.real,no.imaginary)
        x,y = num.real,num.imag
        if y == 0:
            result = "%.2f+0.00i" % (x)
        elif x == 0:
            if y >= 0:
                result = "0.00+%.2fi" % (y)
            else:
                result = "0.00-%.2fi" % (abs(y))
        elif y > 0:
            result = "%.2f+%.2fi" % (x,y)
        else:
            result = "%.2f-%.2fi" % (x, abs(y))
        return result
    def mod(self): 
        num = complex(pow(pow(self.real,2) + pow(self.imaginary,2),0.5))
        x,y = num.real,num.imag
        if y == 0:
            result = "%.2f+0.00i" % (x)
        elif x == 0:
            if y >= 0:
                result = "0.00+%.2fi" % (y)
            else:
                result = "0.00-%.2fi" % (abs(y))
        elif y > 0:
            result = "%.2f+%.2fi" % (x,y)
        else:
            result = "%.2f-%.2fi" % (x, abs(y))
        return result
