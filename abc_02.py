from math import pi
from abc import ABC, abstractclassmethod

class SHAPE(ABC):
    def area(self,length,breadth,radius):
        pass
    def perimeter(self,length,breadth,radius):
        pass

class SQUARE(SHAPE):
    def area(self,length):
        a=length*length
        print(f"area of the square {a}")

    def perimeter (self,length):
        p=4*length
        print(f"perimeter of square {p}")

class RECTANGLE(SHAPE):
    def area(self,length,breadth):
        a=length*breadth
        print(f"area of the rectangle {a}")

    def perimeter(self,length,breadth):
        p=2*(length+breadth)
        print(f"perimeter of rectangle {p}")

class CIRCLE(SHAPE):
    def area (self,radius):
        a=pi*(radius**2)
        print(f"area of circle {a}")

    def perimeter(self,radius):
        p=2*pi*radius
        print(f"circumference of circle {p}")



square=SQUARE()
rectangle=RECTANGLE()
circle=CIRCLE()


square.area(23)
square.perimeter(23)
rectangle.area(23,54)
rectangle.perimeter(23,54)
circle.area(43)
circle.perimeter(43)

    
