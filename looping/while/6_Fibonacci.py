# Fibonacci Series:
#    - Write a Python program to print the Fibonacci series up to a specified number using a `while` loop.

n=int(input("enter the number"))

a,b=0,1

while(a<n):
    
    print(a)
    
    a,b=b,a+b

