number=int(input("enter the number"))

is_prime=True

#factors of number(1,number)

for i in range(2,number):#i=2,3,4,5,6

    if number%i==0:

        is_prime=False

        break
print(is_prime)















