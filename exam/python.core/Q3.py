
def most_frequent_word(text):
    words = text.split()
    word_frequency = {w: words.count(w) for w in words}
    return max(word_frequency, key=word_frequency.get)
text = "Hello world Hello everyone. Welcome to the world."
most_freq_word = most_frequent_word(text.lower())
print("Most Frequent Word:", most_freq_word)
