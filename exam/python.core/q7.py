# Write a Python function that reads a block of text and prints all the words that
#  appear only once (i.e., non-recursive words). The function should ignore case
#  sensitivity and punctuation while identifying the words.
#  Output:
#  text = "Hello world! This is a test. Hello everyone."
#  print_non_recursive_words(text) #world,this,is,a,tes
words=["hello","hai","hello","this","is","this","is","hello","hdqwhdyu"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency)

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)