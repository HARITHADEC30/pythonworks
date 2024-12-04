
from re import fullmatch

adhar_number=input("enter the number=")

pattern="[2-9]{1}[0-9]{3}\s[0-9]{4}\s[0-9]{4}"

matcher=fullmatch(pattern,adhar_number)

if matcher==None:
    print("invalid")

else:
    print("valid")




from re import fullmatch

adhar_number=int(input("enter number"))

pattern="[2-9]{1}[0-9]{3}/s[0-9]{4}/s[0-9]{4}"

matcher=fullmatch(pattern,adhar_number)

if fullmatch==none:
    print("invalid")

else:
    print("valid")