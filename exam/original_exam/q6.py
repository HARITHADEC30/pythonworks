# Write a Python function named next_fibonacci_number(number) that takes an
# integer number as input and returns the next Fibonacci number that is greater than
# number.
# Function Signature: def next_fibonacci_number(number: int) -> int:
# Input: An integer number (where number >= 0).
# Output: The next Fibonacci number after number.
# next_fibonacci_number(5) # should return 8
# next_fibonacci_number(13) # should return 21

def next_fibonacci_number(number):
    prev=0
    current=1
    for i in range(1,number+1):
        next=prev+current
        prev=current
        current=next
    
    return current

number=int(input("eneter the number"))
print(next_fibonacci_number(number))

