# 5. Write a Python program to create a dictionary from a list of keys
#  and values using dictionary comprehension.


keys = ['apple', 'banana', 'cherry']
values = [1, 2, 3]

fruit_dict = {key: value for key, value in zip(keys, values)}

print(fruit_dict)

