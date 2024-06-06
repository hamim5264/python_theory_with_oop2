"""
- Inheritance allows us to define a class that inherits all the properties from another class.
- Parent Class: is the class being inherited from, also called the base class.
- Child Class: is the class that inherits from another, also called derived class.
- Parent class can't take the properties of child class

"""


# Creating Base Class
class BaseClass:
    car = "Supra"
    phone = "IPhone"
    cash = "10M"


# Creating Child Class Where We Inject The Base Class
class ChildClass(BaseClass):
    laptop = "Acer"
    telePhone = "Old Model"


# Creating Object
allAssets = ChildClass()

print(allAssets.car)
print(allAssets.laptop)
