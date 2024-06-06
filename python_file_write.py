"""
"a" - Append- will append to the end of the file
"w" - Write- will overwrite any existing content
"""
# Using w keyword
writeFile = open("Hamim.html", "w")
writeFile.write("<h1> Hello World! </h1>")


# Using a keyword

writeAnotherFile = open("Leon.text", "w")
writeAnotherFile.write("This is me from earth!\n")
writeAnotherFile = open("Leon.text", "a")
writeAnotherFile.write("How are you all?")
writeAnotherFile = open("Leon.text", "r")
print(writeAnotherFile.read())
