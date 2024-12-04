#10. Given a dictionary of items and their prices, write a program to apply a
#  10% discount to all the items using dictionary comprehension.


prices = {'apple': 100, 'banana': 50, 'cherry': 200, 'date': 80}
discount_rate = 0.10

discounted_prices = {item: price * (1 - discount_rate) for item, price in prices.items()}

print(discounted_prices)
