def most_frequent_word(text):

    words=text.split()

    return words.count(w)

frequent_word=max(words,key=most_frequent_word(w))

text = "Hello world! Hello everyone. Welcome to the world."

print(most_frequent_word)
