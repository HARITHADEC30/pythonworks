#15. Write a Python program to split a list into two halves.
arr= [1, 2, 3, 4, 5, 6]
length=len(arr)
mid = length// 2

first_half = arr[:mid]
second_half = arr[mid:]

print("First Half:", first_half)
print("Second Half:", second_half)
