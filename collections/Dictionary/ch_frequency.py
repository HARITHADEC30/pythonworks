text="ABAABC"

#most recursiv character
#non recursiv character

def get_count(char):

    return text.count(char)

most_frequent_charcter=max(text,key=get_count)

print(most_frequent_charcter)

least_recursive_character=min(text,key=get_count)
print(least_recursive_character)

