# to check a number perfect

# def is_perfect(n):
#     total = 0
#     for i in range(1, n):
#         if n % i == 0:
#             total += i
#     if total == n:
#         return f"{n} is a perfect number"
#     else:
#         return f"{n} is not a perfect number"

# print(is_perfect(6))

def is_perfect(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total == n
print(is_perfect(6))