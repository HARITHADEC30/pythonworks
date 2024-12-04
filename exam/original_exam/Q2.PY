# 3. given a string

text = "this is a simple python program that print most recursive word . this program is simple" 

# write a program to print most frequent word
words=text.split()

most_frequent_word=""
max_count=0

for ch in set(words):
    count=words.count(ch)

    if count>max_count:
        most_frequent_word=ch
        max_count=count

print(most_frequent_word)