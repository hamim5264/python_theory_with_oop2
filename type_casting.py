"""
Type casting a process of convert any data type to another data type
"""

# String to int
userId = "5264"
print("Before type casting: ")
print(type(userId))
typeCastStringToInt = int(userId)
print("After type casting: ")
print(typeCastStringToInt)
print(type(typeCastStringToInt))

# Int to string
num1 = 10
print("Before type casting: ")
print(type(num1))
typeCastIntToString = str(num1)
print("After type casting: ")
print(typeCastIntToString)
print(type(typeCastIntToString))

# Int to float
num2 = 10
print("Before type casting: ")
print(type(num2))
typeCastIntToFloat = float(num2)
print("After type casting: ")
print(typeCastIntToFloat)
print(type(typeCastIntToFloat))
