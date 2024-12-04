#student[id,name,course]
#set_student()
#display_student

class student:
    name:str
    rolnumber:int
    age:int
    course:str

    def display_student(self,name,rolnumber,age,course):

        self.name=name
        self.rolnumber=rolnumber
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.rolnumber,self.age,self.course)#CLASS CREATED

#reference_name=ClassName()

student_intance1=student()

student_intance1.display_student("vyshnav",100,35,"django")

student_intance1.display()

#create emplyee,student