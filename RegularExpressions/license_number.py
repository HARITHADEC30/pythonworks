from re import fullmatch

license_number=input("enter the number=")

pattern="(KL)[0-9]{2}\s[0-9]{4}[0-9]{7}"

matcher=fullmatch(pattern,license_number)

if matcher==None:
    print("invalid")

else:
    print("valid")