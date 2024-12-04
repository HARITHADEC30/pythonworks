# 2. given a string

text = "this is a simple question return word with maximum number of characters" 

# write a program that print the word with maimum number of characters

# words=text.split()

# max_word=max(words ,key=len)

# print(max_word)

words=text.split()

max_word=""
max_lenth=0

for w in words:
    if max_lenth<len(w):
        max_word=w
        max_lenth=len(w)

print(max_word)

