def review(rating):
    if rating<0:
        raise Exception("too low")
    elif rating>10:
        raise Exception("too high")
    else:
        print("done!...")

try:
    review(20)
except Exception as e:
    print(e)

print("hai")
print("helo")


# def poll(age):

#     assert age>18,"invalid age"

#     print("voted")

# poll(14)


def poll(age):

    assert age>18,"invalid age"

    print("voted")
try:
    poll(14)

except Exception as e:
    print(e)



def review(rating):
    assert rating>0,"too low"

    assert rating in range(0,11),"too high"

    
print("rated")