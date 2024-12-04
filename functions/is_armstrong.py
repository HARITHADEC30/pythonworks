def is_armstrong_number(number):
    original_number = number
    sum = 0
    power = len(str(number))
    while number > 0:
        digit = number % 10
        sum += digit ** power
        number = number // 10
    return original_number == sum

print(is_armstrong_number(153))


    