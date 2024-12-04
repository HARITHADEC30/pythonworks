arr=[100,200,300,400,500]
k=2
#rotate array k times[500,400,300,200,100]

#k=2[400,500,100,200,300]
for i in range(1,k+1):
    
    popeed_element=arr.pop()
    
    arr.insert(0,popeed_element)

print(arr)
