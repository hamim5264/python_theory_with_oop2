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
print(sportsCar)
print(sportsCar["Company Owner"])

# Using get method
getCarInfo = sportsCar.get("BMW Z4")
print(getCarInfo)

"""
- for only get key, use keys keyword
"""
getKeys = sportsCar.keys()
print(getKeys)

"""
- for only get values, use values keyword
"""
getValues = sportsCar.values()
print(getValues)
