"""
List comprehension is an easy to read, compact,
and elegant way of creating a list from any existing iterable object
"""
myList = [1, 2, 3, 4, 5]
print("Before Comprehension: ", myList)

comprehensionMethod = [eachNumber * 2 for eachNumber in myList]
print("After Comprehension: ", comprehensionMethod)
