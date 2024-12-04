year=int(input("enter year="))

if (year%100==0) or (year%4==0) and (year%100!=0) or (year%4==0):
    print("leap year")

else:
    print("not leap year")


