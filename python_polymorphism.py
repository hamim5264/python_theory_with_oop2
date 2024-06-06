class Vehicle:
    def __init__(self, model, brand, component):
        self.model = model
        self.brand = brand
        self.component = component


class Car(Vehicle):
    pass


carObject = Car("SP1548", "Supra", "Carbon")
print(carObject.model)
print(carObject.brand)
print(carObject.component)


class Phone(Vehicle):
    pass


phoneObject = Phone("11", "Iphone", "Metal")
print(phoneObject.model)
print(phoneObject.brand)
print(carObject.component)
