number=int(input("enter the number="))
total=0

while(number!=0):
    digit=number%10
    digit_squre=digit**2
    total=total+digit_squre
    number=number//10

print(total)
