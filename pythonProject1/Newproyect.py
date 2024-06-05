import math
class GeometricFigure1:
    def calculatearea(self):
        pass
class Rectangle2(GeometricFigure1):
    def __init__(self,height,lenght):
        self.height = height
        self.lenght = lenght
        self.area = self.height * self.lenght
        print("area del rectangulo es",self.area)

class Triangle3(GeometricFigure1):
    def __init__(self,height,base2):
        self.height = height
        self.baseline = base2
        self.area = self.height * self.baseline
        print("area del triangle es",self.area)


class Circle3(GeometricFigure1):
    def __init__(self,radius):
        self.radius = radius
        self.area = math.pi * self.radius ** 2
        print("area del rectangulo es2",self.area)


#crear instanacia

rectangle = Rectangle2(5, 3)
triangle = Triangle3(5, 2)
circle = Circle3(2)
