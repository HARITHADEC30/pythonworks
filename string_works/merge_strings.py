
# text1 = "pqrs"
# text2 = "ABCD"
# result = ""
# i = 0

# while i < len(text1) or i < len(text2):
#     if i < len(text1):
#         result += text1[i]
#     if i < len(text2):
#         result += text2[i]
#     i += 1

# print(result)


text1="HRTA"  # for same length strings

text2="AIH "

result=""

for i in range(0,len(text1)):

    result+=text1[i]+text2[i]

print(result)


text1="PQRST"   # for diffrent length strings
text2="ABC"

smallest_text=text1 if text1<text2 else text2
largest_text=text1 if text1>text2 else text2

result=""

for i in range(0,len(smallest_text)):

    result+= text1[i]+text2[i]

balancw_text=largest_text[len(smallest_text):]

result+=balancw_text

print(result)



# TEXT="abcdades"
# for i in range(0,len(TEXT)):


#COLLECTION DATA TYPE
#LIST
# tuple
# SET

