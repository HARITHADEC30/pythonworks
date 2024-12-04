#print hcf pf two numbers 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

hcf = 0

for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0:
        print(i)
        hcf = i

print("HCF of", num1, "and", num2, "is:", hcf)

