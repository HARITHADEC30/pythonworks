#4. Write a Python program to count the occurrences of each element in a list.
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4,4]
elements = []

for num in numbers:
    if num not in elements:
        elements.append(num)
        occurrence = [num, numbers.count(num)]
        print(occurrence)

