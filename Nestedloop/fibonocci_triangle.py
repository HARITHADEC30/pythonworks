n = 7  # Number of rows

for row in range(1, n + 1):
    a, b = 0, 1  # Initialize the first two Fibonacci numbers
    for col in range(row):
        print(a, end=" ")
        a, b = b, a + b  # Update the Fibonacci sequence
    print()