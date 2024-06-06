"""
- Hierarchical inheritance is a type of inheritance,
- In which multiple classes inherit from a single superclass
"""


# Parent Class/Base Class
class A:
    phone = "Iphone"
    tk = "1Cr"


# Intermediate Class
class B(A):
    car = "Supra"


class C(A):
    house = "Marvel"


# Sub Classes
class D(B, C):
    netIncome = "100$ per month"


allAssets = D()
print(allAssets.phone)
print(allAssets.tk)
print(allAssets.car)
print(allAssets.netIncome)
