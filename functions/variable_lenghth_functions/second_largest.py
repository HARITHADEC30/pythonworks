def second_max(*args):
    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]

print(second_max(10,11,12,13))
print(second_max(89,45,67,34,98,34,65))

#(*args)----->for any number of parameter  will be accepted 
# return as tuple

#(**kwargs)----> return as dictionary

def second_max(*args):
    sorted_numbers=sorted(args,reverse=True)

    return sorted_numbers[1]
print(second_max(10,11,12,13))