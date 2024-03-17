sportsCar = {
    "Subaru BRZ": {
        "MPG": "20 City / 27 Hwy",
        "Engine": "Premium Unleaded H-4 2.4 L/146"
    },
    "Chevrolet Camaro": {
        "MPG": "16 City / 26 Hwy",
        "Engine": "Gas V6 3.6L/222"
    },
    "BMW Z4": {
        "MPG": "25 City / 33 Hwy",
        "Engine": "Intercooled Turbo Premium Unleaded I-4 2.0 L/122"
    },
    "Company Owner": "Hamim",
    "Age": 25
}

# Using pop method
print("Before removed: ", sportsCar)
sportsCar.pop("BMW Z4")
print("After Removed", sportsCar)

# Using popitem method
"""
- popitem method removed the last item of dictionary
"""
print(print("Before removed: ", sportsCar))
sportsCar.popitem()
print("After 1st pop item: ", sportsCar)
sportsCar.popitem()
print("After 2nd pop item: ", sportsCar)

# Using clear method
"""
- clear method also delete the whole dictionary
- and show empty dictionary 
"""
sportsCar.clear()
print(sportsCar)

# Using del method
"""
- del method delete the whole dictionary
- and show error because of the dictionary is no longer exits
"""
del sportsCar
print(sportsCar)
