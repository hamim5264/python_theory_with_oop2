# For loop in list
forLoopList = ["Apple", "Banana", "Cheery", "Jackfruit"]
for eachElement in forLoopList:
    print(eachElement)

# Range & Len loop in list
rangeAndLenLoopList = ["C", "C#", "C++", "Java", "Python"]
for eachElement in range(len(rangeAndLenLoopList)):
    print(eachElement)

# While loop with len in list
whileLoopList = [10, 20, 30, 40, 50, 60]
x = 0  # index is 0
while x < len(whileLoopList):
    print(whileLoopList[x])
    x += 1

# Only While loop
numberList = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
y = 0
while y < 5:
    print(numberList[y])
    y += 1
