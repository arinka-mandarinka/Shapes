import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Shape:
    def __init__(self):
        self.name = ''

    def get_perimeter(self):
        return 0

    def get_area(self):
        return 0

    def get_length_two_point(onePoint, twoPoint):
        return math.sqrt(math.pow(twoPoint.x - onePoint.x, 2) + math.pow(twoPoint.y - onePoint.y, 2))

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.lenFromAToB = Shape.get_length_two_point(a, b)
        self.lenFromBToC = Shape.get_length_two_point(b, c)
        self.lenFromCToA = Shape.get_length_two_point(c, a)
        self.name = 'треугольник'

    def get_perimeter(self):
        return self.lenFromAToB + self.lenFromBToC + self.lenFromCToA

    def get_area(self):
        semi_perimeter = self.get_perimeter() / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - self.lenFromAToB) 
                                        * (semi_perimeter - self.lenFromBToC)
                                        * (semi_perimeter - self.lenFromCToA))

class Circle(Shape):
    def __init__(self, a, b):
        self.lenFromAToB = Shape.get_length_two_point(a, b)
        self.name = 'круг'

    def get_perimeter(self):
        return 2 * math.pi * self.lenFromAToB

    def get_area(self):
        return math.pi * math.pow(self.lenFromAToB, 2)

class Quadrilateral(Shape):
    def __init__(self, a, b, c, d):
        self.lenFromAToB = Shape.get_length_two_point(a, b)
        self.lenFromBToC = Shape.get_length_two_point(b, c)
        self.lenFromCToD = Shape.get_length_two_point(c, d)
        self.lenFromDToA = Shape.get_length_two_point(d, a)
        self.name = 'четырехугольник'

    def get_perimeter(self):
        return self.lenFromAToB + self.lenFromBToC + self.lenFromCToD + self.lenFromDToA

    def get_area(self):
        return self.lenFromAToB * self.lenFromBToC
