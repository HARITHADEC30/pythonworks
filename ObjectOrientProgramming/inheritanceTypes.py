class GrandParant:
    def m1(self):
        print("grand parent class m1 method")

class Parent():
    def m2 (self):
        print("parent class m2 method")

class Child(Parent,GrandParant):
    def m3(self):
        print("child class m3 method")

Child_instanCe=Child()
Child_instanCe.m3()
Child_instanCe.m2()
Child_instanCe.m1()

#in the condition of two same name type the first given class will be printed
#class Child(Parent,GrandParant):
#hear the parent will printed

class GrandParant:
    def m(self):
        print("grand parent class m1 method")

class Parent():
    def m (self):
        print("parent class m2 method")

class Child(Parent,GrandParant):
    def m3(self):
        print("child class m3 method")

Child_instanCe=Child()
Child_instanCe.m3()
Child_instanCe.m()
