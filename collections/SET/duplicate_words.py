text="this is a test to remove duplicate words this test is simple"

#split text withe space

words=text.split(" ")

text2="this simple test remove duplicate words"
words2=text2.split(" ")

is_subset=set(words2).issubset(set(words))
print(set(words))

print(is_subset)

