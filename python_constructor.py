"""
- Parameterized constructor
- Non-Parameterized constructor
- In python, a constructor begins with double underscore(_) and always named as __init__()
- self if by default parameter
"""


# Parameterized Constructor
class studentInfo:
    def __init__(self, name, id):
        print(f"Student Name is: {name} & Id is: {id}")


student1 = studentInfo("Hamim", "221-15-5264")
