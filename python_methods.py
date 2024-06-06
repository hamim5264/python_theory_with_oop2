class studentInfo:
    def __init__(self, name, id):
        print(f"Student Name is: {name} & Id is: {id}")

    # Instance Method
    def UniName(self, uni_name):
        self.UniName = uni_name
        print(uni_name)

    # Classmethod
    @classmethod
    def uniRank(cls):
        print("6")

    # Static Method
    @staticmethod
    def uniStaticMethod():
        print("We are proud to admit here.")


student1 = studentInfo("Hamim", "221-15-5264")
student1.UniName("DIU")
student1.uniRank()
student1.uniStaticMethod()
