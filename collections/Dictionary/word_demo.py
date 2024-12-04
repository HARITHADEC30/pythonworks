text="this is a simple program this program count the word count thi program is simple"

words=["hai","hello","hai","hello","hello"]

word_count={}

for w in words:
    
    if w in word_count:
        word_count[w]+=1

    else:
        word_count[w]=1

print(word_count)
word={}
