# 8. Find the Greatest Common Divisor (GCD):
#    - Write a Python program to find the GCD of two numbers using a `while` loop.

num1=int(input("enter the number"))
num2=int(input("enter the number"))

while(num2!=0):
    temp=num2
    num2=num1%num2
    num1=temp

print(num1)