#starting with alphabet p-t
#in second place mustbe a numer this is \by 3
#followed ny anynumber alphabets,numbers,@

#s6abc
#a6vvhvh
#s7bc

from re import fullmatch

user_input=input("enter variale name=")

pattern="[p-tP-T][369][a-zA-Z0-9@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")