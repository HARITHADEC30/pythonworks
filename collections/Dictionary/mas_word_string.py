text="this is a of simple programming question to find word with maimum number of characters"
words=text.split(" ")
# def get_length(w):
    
#     return len(w)
# print(max(words,key=get_length))

#for sorted ascending order

# def get_length(w):

#     return len(w)

# srt_words=sorted(words,key=get_length,reverse=True)

# print(srt_words)

words=text.split(" ")

def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)
