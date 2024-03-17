sportsCarDictionary = {
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

# Using copy method
print(sportsCarDictionary)
copyOfDictionary = sportsCarDictionary.copy()
print(copyOfDictionary)

# Using dict method
anotherCopyOfDictionary = dict(sportsCarDictionary)
print(anotherCopyOfDictionary)
