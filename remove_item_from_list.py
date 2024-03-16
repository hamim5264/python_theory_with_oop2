"""
Four Ways to remove item from list
1. remove function (where selected item will be removed)
2. pop function (where item can be removed by index)
3. del function (where item can be removed by index also it can remove the whole list)
4. clear function (where the whole list will be deleted)
"""

# Using remove function
fruitList = ["apple", "banana", "mango"]
print(fruitList)
fruitList.remove("apple")
print(fruitList)

# Using pop function
programList = ["C", "Java", "Python"]
print(programList)
programList.pop(0)
print(programList)

# Using del function
courseList = ["GDE", "CSE", "MAT"]
print(courseList)
del courseList[2]
print(courseList)

# Using __delitem__ method
numberList = [1, 2, 3, 4, 5]
print(numberList)
numberList.__delitem__(1)
print(numberList)

# Using clear function
skillList = ["TeamWork", "TimeManagement", "GroupLeader"]
print(skillList)
skillList.clear()
print(skillList)
