"""
A RegEx, or regular expression is a sequence of character that forms a search pattern.
"""

import re

text = "My Girl Guided by A Murderer Who is Me"
findChar = re.findall("[a-l]", text)
print(findChar)

startsWith = "^Girl"
mathStarts = re.findall(startsWith, text)
print(mathStarts)
if mathStarts:
    print("Yes! starts with my")
else:
    print("No!")
