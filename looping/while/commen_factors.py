num1=int(input("enter the number="))

num2=int(input("enter the number="))



# for i in range(1,num1+1):#start from num+1

#     if num1%i==0  and num2%1==0:  #if the modulus is == 0,that is the factor
        

#         print(i)
gcd=1
min_num=num1 if num1<num2 else num2

for i in range(1,min_num):

    if num1%1==0 and num2%i==0:

        gec=i

print(gcd)