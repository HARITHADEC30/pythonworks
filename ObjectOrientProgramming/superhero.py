class superhero:
    def __init__(self,name,suit):
        self.name=name
        self.suit=suit

    def __str__(self):
        return self.name

class spiderman(superhero):

    def __init__(self,name,suit):
        super().__init__(name,suit)

    def super_power(self):
        print("spider sense","web browsing","sticky hands")


class minnalmurali(superhero):
    def __init__(self,name,suit):
        super().__init__(name,suit)

    def super_power(self):
        print("running","jumbing","reflex")


spiderman_instance1=child()
spiderman_instance1.superhero()