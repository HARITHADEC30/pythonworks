class mobile:

    name:str
    brand:str
    price:int

    def __init__(self,name,brand,price):

        self.name=name
        self.brand=brand
        self.price=price

    def display(self):
        print(self.name,self.brand,self.price)

mobile_instance1=mobile("Vivo S1","VIVO",20000)

mobile_instance1.display()

#bank