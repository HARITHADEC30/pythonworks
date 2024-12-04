#2. Sum of First N Natural Numbers:
   #- Write a Python program to calculate the sum of the first N natural numbers using a `while` loop.

number=int(input("ebter the numer="))

factorial=1

while(number>0):
    factorial=factorial*number
    number=number-1
    
print(factorial)
