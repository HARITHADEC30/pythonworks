# num1=int(input("enter the number="))
# num2=int(input("enter the number="))



# max_num = max(num1, num2)
# while True:
#     if max_num % num1 == 0 and max_num % num2 == 0:
#         print("LCM of", num1, "and", num2, "is", max_num)
#         break
#     max_num += 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

max_num=max(num1,num2)

for i in range(max_num,(num1*num2)+1,max_num):

    if i%num1==0 and i%num2==0:

        print(i)

        break




