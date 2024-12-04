# 6. Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair
#  #them together into a dictionary.

fruits = ['apple', 'banana', 'cherry']
prices = [1.99, 0.99, 2.49]

fruit_prices = {fruits[i]: prices[i] for i in range(len(fruits))}

print(fruit_prices)
