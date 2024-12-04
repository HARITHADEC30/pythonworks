#sample input

arr= [100,200,300,400,500,600,700,800]
     #   0    1  2   4   5   6   7   8
#resl=[100,800,300,600,500,400,700,200]

#sample input
#arr = [10,20,30,40,50,60]
     #  0  1  2  4  5  6
#resul=[10,60,30,40,40,20]
#odd_position_elements=[20,40,60]
#reverse_odd_elements=[60,40,20]


#odd_position_elements=[arr[i] for i in range(0,len(arr)) if i%2!=0]

odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_elements.reverse()
#enumerate--->grt oject and index--->itrate
print(odd_position_elements)
i=0
for index,num in enumerate(odd_position_elements):
    arr[index+1]=num

    i+=2
print(arr)

