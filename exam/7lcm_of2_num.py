text=["apple","iphone","orange","potatto","tomatto"]

vowel=[w for w in text if w[0] in ["a","e","i","o","u"]]
print(vowel)

consonents=[w for w in text if w[0] not in ["a","e","i","o","u"]]
print(consonents)

long=max([len(w) for w in text])
longest_word=[w for w in text if len(w)==long]
print(longest_word)

