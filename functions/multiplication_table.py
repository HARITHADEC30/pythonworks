#crate a function multiplication tale(number,n)
#print multipliction table of number till n

def multipliction_table(number,n):

    for i in range (1,n+1):

        print(f"{i} *{number}= {number*i}")



print(multipliction_table(3,50))

def multiplication(number,n):
    for i in range(1,n+1):
        print(f"{i} * {number}={number*i}")

print(multiplication(10,2))
