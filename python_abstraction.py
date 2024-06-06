# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):

    @abstractmethod
    def noOfSides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noOfSides(self):
        print("I have 3 sides")


class Pentagon(Polygon):

    # overriding abstract method
    def noOfSides(self):
        print("I have 5 sides")


class Hexagon(Polygon):

    # overriding abstract method
    def noOfSides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):

    # overriding abstract method
    def noOfSides(self):
        print("I have 4 sides")


# Driver code
R = Triangle()
R.noOfSides()

K = Quadrilateral()
K.noOfSides()

R = Pentagon()
R.noOfSides()

K = Hexagon()
K.noOfSides()
