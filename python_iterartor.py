"""
An iterator is an object that contains a countable number of values.
"""

myList = ["Hamim", "Shahina", "Lima", 5, 10, 15]

iterableList = iter(myList)

# Complex Way to Print

print(iterableList.__next__())
print(iterableList.__next__())

# Easy Way to Print

print(next(iterableList))
print(next(iterableList))
