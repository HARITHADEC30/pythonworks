#. given a string

text = "this is a simple python program that print most recursive word . this program is simple" 

#write a program to print most frequent word



word=text.split()
word_frequency={w:word.count(w) for w in word}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(max(recursive_words))