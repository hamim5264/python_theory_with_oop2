"""
There are two methods in tuple
1. count method (how many times are the value available in tuple)
2. index method (find out the index number by putting value)
"""

numbersTuple = (1, 2, 3, 1, 5, 3, 5, 3, 3, 2, 1, 6, 9, 1, 1, 3, 2, "Hamim", "Hamim", "Leon")
# Count method
countTuple = numbersTuple.count("Hamim")
print(countTuple)

# Index method
indexTuple = numbersTuple.index("Leon")
print(indexTuple)
