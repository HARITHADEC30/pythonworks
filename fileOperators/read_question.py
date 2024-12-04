f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\questions.txt","r")

words=[]
word_frequency={}
for line in f:
    line=line.rstrip("\n")
    all_words=line.split(" ")
    for w in all_words:
        words.append(w)
word_frequency={w:words.count(w) for w in words}
nested_word_count=[[v,k] for k,v in word_frequency.items()]
print("desenting=",sorted(nested_word_count,reverse=True))


print(words)
print(word_frequency)