# # Q4) sort three numbers

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# # Swap numbers if they are in wrong order
# if num1 > num2:
#     num1, num2 = num2, num1
# if num2 > num3:
#     num2, num3 = num3, num2
# if num1 > num2:
#     num1, num2 = num2, num1

# print("Sorted numbers: ", num1, num2, num3)



# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))

# if num1 <= num2 <= num3:
#     print("Sorted numbers: ", num1, num2, num3)
# elif num1 <= num3 <= num2:
#     print("Sorted numbers: ", num1, num3, num2)
# elif num2 <= num1 <= num3:
#     print("Sorted numbers: ", num2, num1, num3)
# elif num2 <= num3 <= num1:
#     print("Sorted numbers: ", num2, num3, num1)
# elif num3 <= num1 <= num2:
#     print("Sorted numbers: ", num3, num1, num2)
# else:
#     print("Sorted numbers: ", num3, num2, num1)




num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
num3=int(input("enter the number3:"))

if num1>num2 and num1>num3:
    if num2>num3:
        print(num1,num2,num3)
    else:
        print(num1,num3,num2)

elif num2>num1 and num2>num3:
    if num1>num3:
        print(num2,num1,num3)
    else:
        print(num2,num3,num1)


elif num3>num2 and num3>num1:
    if num1>num2:
        print(num3,num1,num2)
    else:
        print(num3,num2,num1)

else:
    print("both numers are equal")

    