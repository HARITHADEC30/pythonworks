#14. Write a Python program to replace an element in a list with another element.


arr = [1, 2, 3, 4, 5]
element1 = 3
element2 = 8
index = arr.index(element1)
arr.pop(index)
arr.insert(index, element2)
print(arr)  