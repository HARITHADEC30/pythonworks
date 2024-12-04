#syntax
#if confition:
#  stmt1

#  elif condition2:
#     stmt2

# elif condition3:
#     stmt3

# else condition:
   #defualt stmt  


signal=input("enter signal=").lower()#to change input to lowercase
if signal == "red":
    print("STOP")

elif signal == "green":
    print("GO...")

elif signal == "yellow":
    print("wait !..")

else:
    print("invalid signal")



