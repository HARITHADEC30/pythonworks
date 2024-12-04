#7. Write a Python #program to filter a dictionary, keeping only items with 
# values greater than 50 using dictionary comprehension.

data = {'a': 10, 'b': 60, 'c': 30, 'd': 90, 'e': 20}


filtered_data = {key: value for key, value in data.items() if value > 50}


print(filtered_data)

