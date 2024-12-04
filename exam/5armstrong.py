num=int(input("enter numer="))
original=num
digit_count=len(str(num))
total=0
while(num153!=0):
    digit=num%10
    exponent=digit**digit_count
    total=total+exponent

print(total)
