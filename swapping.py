num1 = 25
num2 = 50
print("Before swapping: ", num1, num2)
swap = num1, num2 = num2, num1
print("After swapping: ", swap)

# Alternative way to swapping
a = 10
b = 20
print("Before swapping a = ", a)
print("Before swapping b = ", b)
a, b = b, a
print("After swapping a = ", a)
print("After swapping b = ", b)
