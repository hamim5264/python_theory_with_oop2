# Using for loop
programsTuple = ("C", "C#", "C++", "Python", "Java", "Dart", "PHP", "Rubby", "GoLang")
for p in programsTuple:
    print(p)

# Using range and len
for p in range(len(programsTuple)):
    print(p)
    print(programsTuple[p])

# Using while loop
i = 0
while i < len(programsTuple):
    print(programsTuple[i])
    i += 1
