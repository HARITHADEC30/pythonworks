# string = "sequence of characters"

# string => object class

# class(design,template,blueprint)

# object

# class str:

#     def casefold(self):
#         pass

#     def capitalize(self):
#         pass

# str_obj=str()

# str_obj.capitalize


# text="helloworld"
# result=text.capitalize()# to capilalize first character
# print(result)

# text="Helloworld"
# print(text.casefold())#  capilalize first character TO LOWER CASE

# text="Helloworld"
# print(text.isalpha())# TO check alphabets 

# text="Helloworld"
# print(text.isdigit())# TO check number

# text="Helloworld"
# print(text.isalnum())# TO check alphabets and number

# text="halloworld"
# print(text.startswith("he"))#to check starts with
# print(text.endswith("ai"))#to check ends with

# text="halloworld"
# for ch in text:
#     print(ch)



# text="hello,world,python"
# words=text.split(",")# for split strings
# print(words)

# text="\t hello \t world \t"
# new_text=text.strip("\t") #for remove the \t from leaft and right sides
# print(new_text)           
#  #lstrip() for strip from left side only
#  #rstrip() for strip from right side only

# text="hello world python"
# new_text=text.replace("o","a",2)#for replacing
# print(new_text)


# text="python programming"

# #string_object[start:end:step]

# print(text[0:6]) #python
# print(text[7:18])#programming
# print(text[:6])
# print(text[7:])
# print(text[::2])

# string="hello"
# reversed_text=string[::-1]
# print(reversed_text)

text="helloworld"
print(text.index("o"))

#text.index("o")---> 4

text="vipinkumar@gmail.com"
index=text.index("@")
new_text=text[0:index]
print(new_text)    #print(text[0:text.index("@")])

text="hellopython"

index=text.index("o")

reversed_sub_str=text[index-1::-1]

balance_sub_str=text[index:]

result=reversed_sub_str+balance_sub_str
print(result)

#SAMPLE INPUT 1
# text=pqrs
# tetxt2=ABCD 

# #MERDE TWO STRINGS
# OUTPUT PAQBRCST

# #SAMPLE INPUT2

# TEXT1=PAQRST 
# TEXT2=ABC 

# OUTPUT=PAQBRCST