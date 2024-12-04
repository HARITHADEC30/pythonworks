text="on june 5th,2024,we will celebrate @ our annual event: 'Tech Innovations 2024!'"

#count of alphabets
#count of vowels
#count of special charcter
#count of numbers

count_vowels=0
alphabets=("abcdefghijklmnopqrstuvwxyz")
count_alphabets=0
vowel_sequence=("a,e,i,o,u")
for ch in text:
    if ch in vowel_sequence:

        count_vowels=count_vowels+1

    else:
        count_vowels+=1

print("vowels=",count_vowels)

if ch==alphabets:
    count_alphabets=count_alphabets+1
else:
    count_alphabets+=1

print(count_alphabets)


