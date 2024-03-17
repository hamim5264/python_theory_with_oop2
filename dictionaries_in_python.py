"""
- Dictionaries are used to store data values in key:value pairs
- Ordered and changeable
- Don't allow duplicate value
"""

studentInformation = {
    "Hamim": {
        "Education": "B.Sc in CSE",
        "Age": "22",
        "Id": "221-15-5264",
        "Phone No": 1724879284
    },
    "Leon": {
        "Education": "B.Sc in EEE",
        "Age": "21",
        "Id": "221-15-4254",
        "Phone No": 1476465655
    },
    "Antony": {
        "Education": "B.Sc in SWE",
        "Age": "24",
        "Id": "221-15-5487",
        "Phone No": 147565995
    },
}
print(studentInformation)
print(studentInformation["Hamim"])
print(studentInformation["Leon"]["Phone No"])
