begin = int(input("enter starting limit="))
end= int(input("enter the ending limit="))

# if begin>end:
#     begin,end=end,begin
# i=begin
# while(i<=end):
#     if i%2!=0:
#         print(i)
#     i=i+1

#read  two limit

reverse =True if begin>end else False
i=begin
while(i<=end if reverse == False else i>=end):
    if i%2==0:
        print(i)
    if reverse==False:

        i=i+1
    else:
        i=i-1

reverse=True if begin>end else False
i=begin
while(i<=end if reverse==False else i>=end):
    if i%2==0:
        print(i)
    if reverse==False:
        i=i+1
    else:
        i=i-1