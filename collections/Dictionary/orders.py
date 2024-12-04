orders=["tea","coffee","tea","cofee","gheeroast","plainroasrt","porotta","tea"]

order_summery={}
for w in orders:
    if w in order_summery:
        order_summery[w]+=1

    else:
        order_summery[w]=1

print(order_summery)

# def order_summary(orders):  # Corrected function name and parameter
#     order_summary = {}  # Corrected dictionary name
#     for item in orders:
#         if item in order_summary:
#             order_summary[item] += 1
#         else:
#             order_summary[item] = 1
#     return order_summary  # Return the dictionary

# orders = ["tea", "coffee", "tea", "coffee", "gheeroast", "plainroast", "porotta", "tea"]
# print(order_summary(orders))
