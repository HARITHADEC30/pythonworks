class car:

    name:str

    rand:str

    fual_type:str

    def __init__(self,name,brand,fual_type):
        self.name=name
        self.brand=brand
        self.fual_type=fual_type

    def display(self):
        print(self.name,self.brand,self.fual_type)

    def __str__(self):
        return self.name

car_instance1=car("swift","suzuki","petrol")
car_instance1.display()

#string representtion of a object
#__str__(self)