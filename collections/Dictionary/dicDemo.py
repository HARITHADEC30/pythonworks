#records are stored in pairs of key:value pairs
#key:value

product={"id":1000,"tittle":"phone","price":100000,"brand":"vivo"}

# print(product["price"])

# print(product["brand"])

# #update product price as 20000

# product["price"]=20000
# print(product)

# #update brand as oppo

# product["brand"]="oppo"
# print(product)

# #adding a mew key:value

# product["use_by_date"]="12-10-2024"
# print(product)

# product["offer"]="10%"
# print(product)


#check key exist or not exist
# if "price" in product:
#     print("exist")

# else:
#     print("not exist")

#add offer as 10 if offer exist else add offer as 20

if "offer" in product:

    product["offer"]=10

else:
    product["offer"]=20

print(product)
