# Logical operator
a = 5
b = 5
result = a <= 5 and b >= 10
print(result)
result2 = a == 5 or b == 10
print(result2)
result3 = not (a == 10 and b == 10)
print(result3)

# Example of maximum number between three number
num1 = 10
num2 = 20
num3 = 30
if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num3)
else:
    print(num3)

# Example of vowel check
inputCharacter = input("Please enter a character:\n")
if (inputCharacter == "a" or inputCharacter == "e" or inputCharacter == "i"
        or inputCharacter == "o" or inputCharacter == "u" or inputCharacter == "A"
        or inputCharacter == "E" or inputCharacter == "I" or inputCharacter == "O"
        or inputCharacter == "U"):
    print("Vowel")
else:
    print("Consonant")
