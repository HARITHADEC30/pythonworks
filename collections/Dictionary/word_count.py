text="ABBACB"
#PRINT CHARACTER COUNT
# ch_count={}
# for ch in text:
#     if ch in ch_count:
#         ch_count[ch]+=1
#     else:
#         ch_count[ch]=1
# print(ch_count)
#first recursive charcter

#PRINT CHARACTER COUNT
ch_count={}
for ch in text:
    if ch in ch_count:
        print(ch)

        break
    else:
        ch_count[ch]=1


words=["hello","hai","hello","this","is","this","is","hello","hdqwhdyu"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)

#display non recursive_words
non_recursive_words=[k for k,v in word_frequency.items() if v==1]
print(non_recursive_words)

most_recursive=[]