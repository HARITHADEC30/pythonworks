arr=[2,3,4,5,7,8,9]

# sum=7          ---> the complexity is very hight so have another method

# for i in range(0,len(arr)-1):

#     for j in range(i+1,len(arr)):

#         current_sum=arr[i]+arr[j]

#         if sum == current_sum:

#             print(arr[i],arr[j])

#             break
sum=8
left=0
right=len(arr)-1

while(left<right):

    current_sum=arr[left]+arr[right]

    if current_sum==sum:
        print(arr[left],arr[right])
        
        break
    elif current_sum > sum:
        right=right-1

    elif current_sum < sum:
        left=left+1
        
         
#algorithem
# left->0
# right-->len(arr)-1
# loop left<right:
# current_sum==arr[left]+arr[right]
# if current_sum==sum --->print then break
#    current_sum>sum---->right-1
#    current_sum<sum---->left+1

