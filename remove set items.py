"""
Four ways to remove items from set
1. remove function (if the value is not exist then it will show error)
2. discard function (not depends on thw value is exits or not)
3. pop function (you don't know which item will be removed)
4. clear function (all value will be deleted)
"""

programmingSet = {"C", "C#", "C++", "Java", "Python"}

# Using remove function
print(programmingSet)
programmingSet.remove("C")
print(programmingSet)

# Using discard function
programmingSet.discard("Dart")
"""
- here dart is not exists in set but this will not hamper to execute the output
"""
print(programmingSet)

# Using pop function
mySet = {"Apple", "Banana", "Orange"}
print(mySet)
mySet.pop()
print(mySet)

# Using clear function
mySet.clear()
print(mySet)
