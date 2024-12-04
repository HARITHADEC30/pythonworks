#lambda function
#
#lambda function for a adding two numbers

add=lambda n1,n2:n1+n2

print(add(10,4))

#substarction

sub=lambda n1,n2:n1-n2

print(sub(10,4))

#cube

cube=lambda n:n**3

print(cube(3))


max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2
print(max_two("hai","hallo"))

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2
print(min_two("hai","hallo"))


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1
print(smart_sub(4,10))


words=["hello","hai","morning","test","apple"]

# def get_length(word):
#     return len(word)

get_length=lambda word:len(word)
print(max(words,key=get_length))