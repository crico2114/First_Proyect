import math

class geometricfigure:
    def calculatearea(self ):
        pass

class Rectangle :
    def __init__(geometricfigure):
        self.height = height
        self.lenght = lenght
    def calculatearea(self):
        return self.height * self.lenght

class Triangle:
    def __init__(geometricfigure):
        self.height = height
        self.baseline = lenght

    def calculatearea(self):
        return (self height * self.baseline / 2


class Circle:
    def __init__(geometricfigure):
        self.radius = radius

    def calculatearea(self):
        return (self.radius * self.radius)

Recta = Rectangle(5, 3)
Trian = Triangle(2, 2)
Circ = Circle(10)


figure1 = Recta
Figure2 = Trian
figure3 = Circ


print("area del rectangulo es",figure1.calculatearea())

#------------------------------------------------------------------------

class GeometricFigure1:
    def calculatearea(self):
        pass
class Rectangle2(geometricfigure1):
    def __init__(self,height,lenght):
        self.height = height
        self.lenght = lenght
        self.area = self.height * self.lenght
        print("area del rectangulo es",self.area)

class Triangle3(geometricfigure):
    def __init__(self,height,base2):
        self.height = height
        self.baseline = base2
        self.area = self.height * self.baseline
        print("area del triangle es",self.area)


class Circle3(geometricfigure):
    def __init__(self,radius):
        self.radius = radius
        self.area = self.radius * self.radius
        print("area del rectangulo es",self.area)

#crear instanacia

rectangle = Rectangle2(5, 3)
triangle = Triangle3(5, 2)
circle = Circle3(10)
print("area del rectangulo es",rectangle.calculatearea())
print("area del triangulo es",triangle.calculatearea())
print("area del circulo es",circle.calculatearea())







