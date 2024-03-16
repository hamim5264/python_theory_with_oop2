# Break statement
i = 1
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print("Program end")

# Continue statement
j = 1
while j <= 10:
    print(j)
    j = j + 1
    if j == 7:
        continue
print("Program end")
