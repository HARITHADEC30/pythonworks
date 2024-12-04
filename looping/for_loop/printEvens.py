#print start and end 

start=int(input("enter the number:"))
end=int(input("enter the number:"))

#sequnce=range(start,end+1,1)

# for num in range(start,end+1,1):  
#     print(num)

#FOR REVERSE

if start<end:

    for num in range(start,end+1,1):

        print(num)

else:
    for num in range(start,end-1,-1):

        print(num)