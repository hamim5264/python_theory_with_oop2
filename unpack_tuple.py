"""
two ways to unpack tuple:
1. extract the values
2. using asteriks sign
- note that while unpacking make sure that the value of extract should be same as tuple value
"""

# Using extract method
rawTuple = ("Orange", "Banana", "Cherry")
print("Raw tuple: ", rawTuple)
print("Extract tuple:")
(a, b, c) = rawTuple
print(a)
print(b)
print(c)

# Using asteriks sign
programsTuple = ("C", "C#", "C++", "Python", "Java", "Dart", "PHP", "Rubby", "GoLang")
print(programsTuple)
(*p,) = programsTuple
print(p)
(a, b, c, *p,) = programsTuple
print(p)
print(a)
print(b)
print(c)
