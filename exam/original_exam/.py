text = "On June 5th, 2024, we will celebrate @ our annual event: 'Tech Innovations 2024!'"
alphabets=sum(1 for ch in text if ch.isalpha)
spaces_count = sum(1 for char in text if char.isspace())
special_chaharcter=sum(1 for ch in text if not ch.isalnum)
numbers_count=sum(1 for ch in text if ch.isdigit)
print(alphabets)
print(spaces_count)
print(special_chaharcter)
print(numbers_count)