class StudentInfo:
    def __init__(self, name, id):
        self.__name = name
        self.id = id
        print(self.__name)


student1 = StudentInfo("Hamim", "5264")
print(student1.id)
