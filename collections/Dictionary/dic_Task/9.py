#9. Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.
data = {'a': -10, 'b': 60, 'c': -30, 'd': 90, 'e': -20}


absolute_data = {key: abs(value) for key, value in data.items()}
print(absolute_data)

