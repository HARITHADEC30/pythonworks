arr=[10,8,7,12,13,20,25]
#read search element
search_element=int(input("enter the search element="))
is_present=False

#step1 sort array
arr.sort()

#step2 set low,upp

low=0
upp=len(arr)-1
while(low<upp):
    #find mid
    mid=(low+upp)//2
    #case 1
    if search_element==arr[mid]:
        is_present=True
        break

    elif search_element<arr[mid]:
        upp=mid-1
    
    elif search_element>arr[mid]:
        low=mid+1

print(is_present)

