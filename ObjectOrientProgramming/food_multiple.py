class Cusine:
    def __init__(self,cusine_name):
        self.cusine_name=cusine_name
        

    def display_cusine(self):
        print(self.cusine_name)

class MealType:
    def __init__(self,name):
        self.name=name

    def display_MealType(self):
        print(self.name)

class Dish(Cusine,MealType):
    dish_name:str
    def __init__(self,cusine_name,name,dish_name):
        Cusine.__init__(self,cusine_name)
        MealType.__init__(self,name)
        self.dish_name=dish_name

    def display_dish_info(self):
        self.display_cusine()
        self.display_MealType()
        print(self.dish_name)


dish_instance=Dish("Indian","Lunch","Dosa")
dish_instance.display_dish_info()
        

