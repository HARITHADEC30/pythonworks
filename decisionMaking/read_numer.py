#read a number 
# print fizz if num / by 3
# print buzz if num / by 5
# print fizzbuzz if num / by 15
# default invalid numer

number=int(input("enter numer="))

if number%15==0:# first give bigger one
    print("fizzbuzz")

elif number%5==0:
    print("buzz")

elif number%3==0:
    print("fizz")

else:
    print("invalid number")