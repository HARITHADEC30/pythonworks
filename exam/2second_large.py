num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num2,"second largest")
    else:
        print(num3,"second largest")
elif num2>num1 and num2>num3:
    if num1>num3:
        print(num1,"second largest")
    else:
        print(num3,"second largest")
elif num3>num2 and num3>num1:
    if num1>num2:
        print(num1,"is second largest")
    else:
        print(num2,"is second largest ")
