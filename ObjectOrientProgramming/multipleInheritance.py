class Person:
    name:str
    age=int
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person_info(self):
        print(self.name,self.age)

class Employee:
    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def display_emp_info(self):
        print(self.emp_id,self.salary)

class Manager(Person,Employee):
    def __init__(self,age,name,emp_id,salary,department):
        Person.__init__(self,age,name)
        Employee.__init__(self,emp_id,salary)
        self.department=department

    def display_manager_info(self):
        
        self.display_person_info()
        self.display_emp_info()
        print(self.department)


Manager_instance=Manager(32,"hari","eol",54000,"HR")
Manager_instance.display_manager_info()
        

