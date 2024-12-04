n1=int(input("enter the number1="))
n2=int(input("enter the number2="))
n3=int(input("enter the number3="))

if n1>n2 and n1>n3:
    print(n1," largest number")
elif n2>n1 and n2>n3:
    print(n2," largest number")
elif n3>n1 and n3>n2:
    print(n3," largest number")
elif n1==n2 and n2==n3:
    print("bothe numers are equal")
