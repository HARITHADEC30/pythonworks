lst1=["apple","mango","onion","pottato"]
lst2=[100,200]

result={}
num=1
for i in range(0,len(lst2)):
    list_one_index=lst1[i]
    list_two_indexx=lst2[i]

    result[list_one_index]=list_two_indexx

print(result)

balnced_element=lst1[len(lst2):]
for index,element in enumerate(balnced_element):
    result[element]=index+i

print(result)

