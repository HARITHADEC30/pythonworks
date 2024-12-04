#SILENT AND LISTEN

text1="silent"
text2="listen"

is_anagram=True
for ch in text1:
    if ch not in text2:
        is_anagram=False
        break
print(is_anagram)















