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

# loop in keys
for keys in sportsCar:
    print(keys)

# Alternative loop for keys
for eachKeys in sportsCar.keys():
    print(eachKeys)

# loop in values
for values in sportsCar.values():
    print(values)

# loop in keys and values using items keyword
for singleKeys, singleValues in sportsCar.items():
    print(singleKeys, singleValues)
