def display_mobile_data(**kwargs):

    print(kwargs.get("name"))
    print(kwargs.get("price"))

display_mobile_data(name="oneplus",price=32000,display="amoled")

#calculator(10,20,30,operation="+")
#and also  operation="*"
def calculator(*args,**kwargs):
    if kwargs.get("operation")=="+":
        return sum(args)

    if kwargs.get("operation")=="*":
        result=1
        for num in args:
            result=result*num
        return result

print(calculator(10,20,30,operation="*"))

#def student_info(4543,44,operation="avg")

def student_info(*args,**kwargs):
    if kwargs.get("operation")=="avg":
        
        return sum(args)/len(args)

    if kwargs.get("operation")=="total":
        return sum(args)

print(student_info(14,43,44,operation="avg"))

#def sort_numbers(1,2,3,4,15,11,reverse=True)desc
#def sort_numbers(1,2,3,4,15,11,reverse=False)asec

def sort_numbers(*args,**kwargs):
    if kwargs.get("reverse")=="True":
        return sorted(args,reverse=True)

    if kwargs.get("reverse")=="False":
        return sorted(args)
    

print(sort_numbers(1,2,6,4,15,11,reverse="True"))
print(sort_numbers(1,2,6,4,15,11,reverse="False"))





