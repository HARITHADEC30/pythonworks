#list comprehnsion

arr=[2,3,4,5,6,7]

#cubes
#cubes=[]
#for num in arr:
#    cubes.append(arr**3)
#print(cubes)


# #refernce=[return loop condition]
# cubes=[num**3 for num in arr]
# print(cubes)

# add_five=[num+5 for num in arr]

# print(add_five)

# #list comprention------------------------------>
#arr=[2,3,4,5,6,7]
# squares=[num**2 for num in arr]
# print(squares)


#list compretion--------------------------------->


#mapping
#filter
#reduce

#[[hari,hr,25000],[vipin,it,27000],[binoy,hr,26000]]

# arr=[2,3,4,5,6,7]
# #   [1,2,3,6,7,8]

# mapp_num= [num+1 if num>5 else num-1 for num in arr]


# #return itration condition
# add_ten=[num+10 for num in arr]
# print(add_ten)

# odd_numbers=[num for num in arr if num%2!=0]
# print(odd_numbers)

# even_numbers=[num for num in arr if num%2==0]
# print(even_numbers)


# num_dt_five=[num for num in arr if num>5]
# print(num_dt_five)

#return a new list num+1 if num>5 else num-1

text=["apple","iphone","orange","potatto","tomatto"]

#words starting with vowels

vowel_words=[w for w in text if w[0] in ['a','e','i','o','u']]
print(vowel_words)
consonant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]
print(consonant_words)

#longest words

long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)