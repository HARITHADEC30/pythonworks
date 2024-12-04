#polymorphism
class Shipping:
    def calculate_shipping_cost(self,weight):
        print(weight*5)

class ExpressShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*20)

class StanderdShipping(Shipping):
    def calculate_shipping_cost(self,weight):
        print(weight*10)

ExpressShipping_instance=ExpressShipping()
ExpressShipping_instance.calculate_shipping_cost(10)
StanderdShipping_instance=StanderdShipping()
StanderdShipping_instance.calculate_shipping_cost(10)