#  Write a Python function named next_fibonacci_number(number) that takes an
#  integer number as input and returns the next Fibonacci number that is greater than
#  number.
#  Function Signature: def next_fibonacci_number(number: int) -> int:
#  Input: An integer number (where number >= 0).
#  Output: The next Fibonacci number after number.
#  next_fibonacci_number(5)  # should return 8
#  next_fibonacci_number(13) # should return 2

   
def next_fibonacci_number(number: int) -> int:
    # Start with the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    
    # Generate Fibonacci numbers until we find one greater than `number`
    while b <= number:
        a, b = b, a + b  # Move to the next Fibonacci numbers
    
    return b  # `b` is now the next Fibonacci number greater than `number`
print(next_fibonacci_number(5))   # Output: 8
print(next_fibonacci_number(13))