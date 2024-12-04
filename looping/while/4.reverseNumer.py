# 4. Reverse a Number:
#    - Write a Python program to reverse a given number using a `while` loop.

number = int(input("enter the number="))  # Get the number from the user and convert it to an integer

reversed_number = 0  # Initialize the reversed number as 0

while number > 0:  # Loop as long as the number is greater than 0
    last_digit = number % 10  # Get the last digit of the number
    reversed_number = reversed_number * 10 + last_digit  # Add the last digit to the reversed number
    number = number // 10  # Remove the last digit from the number

print("the reversed number is=", reversed_number)  # Print the reversed number
