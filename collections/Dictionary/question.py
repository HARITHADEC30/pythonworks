arr=[10,20,30,40,2,3]
# #{10:100,20:40....}
result={}
for num in arr:
    square=num**2
    result[num]=square

#print(result)
#dictionary compration    
results={num:num**3 for num in arr}

#print(results)  

#results={key:value itration condition}

#new dictionarys even_squrs and odd_cubes

even_squres={num:num**2 for num in arr if num%2==0}
#print(even_squres)

odd_cubes={num:num**3 for num in arr if num%2!=0}

#print(odd_cubes)

#frequncy count of numbers

arr1=[10,20,30,40,2,3,7,8,9,10,30]

frequency_count={num:arr1.count(num) for num in arr}

print(frequency_count)