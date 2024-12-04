expenses=[10000,11000,12000,13000]

# for exp in expenses:

#     print(exp)

#for total

total=0

for exp in expenses:

    total+=exp

print(total)

#to find maximum
max_expenses=0

for ep in expenses:#13000

    if exp> max_expenses: #comparing   13000>0

        max_expenses=exp   #13000

print(max_expenses)


min_expenses=expenses[0]

for exp in expenses:

    if exp<min_expenses:

        min_expenses=exp

print(min_expenses)



#average
#most frequnt exp