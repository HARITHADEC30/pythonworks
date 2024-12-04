# Question 2
#  Count Vowels in a String
#  Write a Python function named count_vowels(string) that takes a string as input
#  and returns the number of vowels (a, e, i, o, u) in that string.
#  Function Signature: def count_vowels(string: str) -> int:
#  Input: A string string.
#  Output: An integer representing the number of vowels in the string.
#  count_vowels("hello world")  # should return 3

def count_vowels(input_str):
    vowel_count = 0
    vowels = ("a", "e", "i", "o", "u")
    for ch in input_str:
        if ch in vowels:
            vowel_count += 1
    return vowel_count

text = "Hello world"
vowel_count = count_vowels(text.lower())
print("Vowel Count:", vowel_count)

