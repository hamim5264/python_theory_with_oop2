i = 1
while i <= 10:
    print(i)
    i += 1
print("Program end")

# Example of even number between 1 - 100
print("Even numbers are:")
x = 2
while x <= 100:
    print(x)
    x += 2

# Example of odd number between 1 - 100
print("odd numbers are:")
x = 1
while x <= 100:
    print(x)
    x += 2

# Sum of n numbers from user input
inputNumer = int(input("Enter the last number:\n"))
sumOfNumbers = 0
y = 1
while y <= inputNumer:
    sumOfNumbers = sumOfNumbers + y
    y += 1
print(sumOfNumbers)
