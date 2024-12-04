from re import fullmatch

user_input=input("enter variable name=")#num_
#start with aplhabets
#any number of alphabets ,digits
pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)#None

if matcher==None:
    print("invalid")
else:
    print("valid")
