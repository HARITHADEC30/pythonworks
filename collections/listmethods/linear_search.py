# searching
# 1)linear
# 2)binary


arr=[2,4,6,3,8,7]

search_element=int(input("enter number="))#2

is_present=False
 
for i in range(0,len(arr)):

    if search_element==arr[i]:

        is_present=True
        break

print(is_present)
