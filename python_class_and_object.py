"""
- Class is a blueprint of an object also class holds many properties
- Object is a property which holds many variables
"""


# Creating Class
class StudentInformation:
    name = ""
    id = ""
    phn = ""


# Creating Object
student1 = StudentInformation()
student1.name = "Hamim"
student1.id = "5264"

# Creating Another Object
student2 = StudentInformation()
student2.phn = 879284

print(f"Student Name: {student1.name}")
print(f"Student ID: {student1.id}")
print(f"Student Phone: {student2.phn}")
