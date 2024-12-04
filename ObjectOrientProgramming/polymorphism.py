#polymorphism(more then one form)
#   method_overloading
#   method_overriding

#method_overloading--->same method name and different number of pararmeters

class Operation:
    
    def add(self,num1,num2):
        print(num1+num2) 

    def add(self,num1,num2,num3):
        print(num1+num2+num3)

obj=Operation()
obj.add(10,20,30)
#heare last given condition will print not first
#obj.add(10,20)#error
#method_overloading not supported in python

#MRTHOD OVERRIDING------->min 2 classes 
                        # thos classes should be inherited
                        # signature should be same

class parent:

    def mobile(self):
        print("nokiax2")

class child(parent):
    def mobile(self):
        print("iphone")

child_instance=child()
child_instance.mobile()
