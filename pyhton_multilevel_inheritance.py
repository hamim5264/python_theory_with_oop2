"""
-The inheritance in which a class can be derived from another derived class is known as Multilevel Inheritance.
-Suppose there are three classes A, B, and C. A is the base class that derives from class B.
-So, B is the derived class of A.
-Now, C is the class that is derived from class B
"""


class A:
    phone = "Iphone"
    balance = "1Cr"


# Derived class of A
class B(A):
    car = "Supra"


# Derived class of B
class C(B):
    house = "Marvel"


# Creating Object
assets = C()
print(assets.phone)
print(assets.balance)
print(assets.car)
print(assets.house)
