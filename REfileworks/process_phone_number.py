from re import fullmatch

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\phone_numers.txt")

for line in f:
    phone=line.rstrip("\n")

    pattern="(91)?[0-9]{10}"

    matcher=fullmatch(pattern,phone)

    if matcher!=None:

        print(phone)