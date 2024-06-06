"""
If a class inherits from many classes inside the parentheses()
then it called multiple inheritance
"""


# Creating class 01:
class Phone1:
    phoneName = "Iphone"
    ram = "4GB"


# Creating class 02:
class Phone2:
    rom = "128GB"


# Creating class 03:
class Phone3:
    launchYear = "2006"


# Inheritance
class Technology(Phone1, Phone2, Phone3):
    models = "XS, XR, 11 Pro"


allTechnologies = Technology()
print(allTechnologies.phoneName)
print(allTechnologies.ram)
print(allTechnologies.rom)
print(allTechnologies.launchYear)
print(allTechnologies.models)
