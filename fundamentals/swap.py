#crate a python file swap.py
#num1=100
#num2=200
#write a python program to print swap thease two numers

num1=100
num2=200
print(f"values before swapping num1={num1},num2={num2}")

# temp=num1
# num1=num2
# num2=temp

#num1,num2=num2,num1

# print(f"values after swapping num1={num1}, num2={num2}")

#logic 2

num1=num1+num2 #num1=100+200=300
num2=num1-num2# num2=300-200=100
num1=num1-num2 #num=300-100=200

print(f"values after swapping num1={num1}, num2={num2}")