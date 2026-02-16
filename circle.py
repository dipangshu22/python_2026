import math

class circle:
    def __init__(self,r):
        self.r=r

    def area(self):
        print("area of the circle is",22/7*math.sqrt(self.r))

    def perimeter(self):
        print("perimeter of the circle is",2*22/7*self.r)

s1=circle(21)
s1.area()
s1.perimeter()