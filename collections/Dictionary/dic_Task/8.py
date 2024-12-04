#Given a sentence, count the frequency of each word using a dictionary.
words=["hello","hai","hello","this","is","this","is","hello","hdqwhdyu"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency)
