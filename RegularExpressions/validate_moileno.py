from re import fullmatch

user_input=input("enter the number=")

pattern="(91)+[0-9]{10}" # ? optional varam varandirikkam
                         # + should be present for one time 
matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")