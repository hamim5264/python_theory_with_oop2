"""
- List a structure where we can keep multiple data & also it is mutable
- List items can be of any data type
"""
myProgrammingList = ["C", "Java", "C#", "Python"]
myNumberList = [1, 2, 3, 4, 5]
myBooleanList = [True, False, True, False]
print(myProgrammingList)
print(type(myProgrammingList))
print(myNumberList)
print(type(myNumberList))
print(myBooleanList)
print(type(myBooleanList))

# Specifically print one item from list
print(myNumberList[2])

# Change index value of list
print(myBooleanList)
myBooleanList[0] = False
print(myBooleanList[0])
print(myBooleanList)
