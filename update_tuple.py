"""
To update tuple:
- convert the tuple into list
- add items as per you want
- them convert it back into a tuple
- you can also change the value of tuple by convert it list
"""

fruitsTuple = ("Orange", "Mango", "Cheery", "Jackfruit")
print(fruitsTuple)
print(type(fruitsTuple))
updatedTuple = list(fruitsTuple)
print(type(updatedTuple))
updatedTuple.append("Banana")
print(updatedTuple)
fruitsTuple = tuple(updatedTuple)
print(fruitsTuple)
print(type(fruitsTuple))

# Example of change item in tuple
numberTuple = (1, 5, 10, 12, 3)
print("Before changing the value: ", numberTuple)
updatedNumberTuple = list(numberTuple)
updatedNumberTuple[2] = 20
print("After changing the value: ", updatedNumberTuple)
numberTuple = tuple(updatedNumberTuple)
print("Now the tuple is: ", numberTuple)
