# If statement
x = 10
myNumberRange = range(5)
if x > 5:
    for i in myNumberRange:
        print(myNumberRange[i])

# If Else statement
studentMarks = 85
if studentMarks >= 33:
    print("Pass")
else:
    print("Fail")

# Example of large number
num1 = 10
num2 = 20
if num1 > num2:
    print(num1)
else:
    print(num2)

# Example of even odd number
inputNumber = input("Enter a number: \n")
inputNumber = int(inputNumber)
if inputNumber % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Elif statement
print("Daffodil International University Grade System :)")
inputMarks = input("Enter your marks: \n")
inputMarks = int(inputMarks)
if inputMarks >= 80:
    print("A+")
elif inputMarks >= 75:
    print("A")
elif inputMarks >= 65:
    print("A-")
elif inputMarks >= 60:
    print("B+")
elif inputMarks >= 55:
    print("B")
elif inputMarks >= 50:
    print("B-")
elif inputMarks >= 45:
    print("C+")
elif inputMarks >= 40:
    print("C")
elif inputMarks >= 35:
    print("D")
else:
    print("Sorry! failed.")