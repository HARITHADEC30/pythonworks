text="malayalam"
#     123456789
length=len(text)-1#9-1=8

reversed_string=""

for i in range(length,-1,-1):

    reversed_string+=text[i]

print(reversed_string)