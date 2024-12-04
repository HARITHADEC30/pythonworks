#__init__() => constructor attributes initialise 

#__str__()  => object string reprasentation

#self       =>point  current instance

#super()    => refer the parent class 

#inheritance => childe class accure the methods and proprties from parent class 

class Animal:
    name:str
    sepecies:str

    def __init__(self,name,species):
        self.name=name
        self.sepecies=species

    def __str__(self):
        return self.name

class lion(Animal):
    def __init__(self,name,species):
        super().__init__(name,species)

    def sound(self):
        print("roar")

lion_instance=lion("lion","carnivorous")
print(lion_instance)
print(lion_instance.sound())





