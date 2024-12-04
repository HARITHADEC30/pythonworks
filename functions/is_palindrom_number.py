def is_palindrome_number(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10
    return original_number == reversed_number

print(is_palindrome_number(12321))  # True


def is_palindrome_number(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        last_digit = number % 10
        reversed_number = reversed_number * 10 + last_digit
        number = number // 10
    if original_number == reversed_number:
        print("The number is a palindrome")
    else:
        print("Not a palindrome")
    return original_number == reversed_number

is_palindrome_number(12321)