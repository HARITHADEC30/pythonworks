# 5. Check for Palindrome:
#    - Write a Python program that checks if a given number is a palindrome using a `while` loop.

number=int(input("enter the number="))

original_number=number
reversed_number=0

while(number>0):
    last_digit=number%10
    reversed_number=reversed_number*10+last_digit
    number=number//10

print("reversed number is",reversed_number)

if original_number==reversed_number:
    print("the number is palindrome")

else:
    print("not palindrome")