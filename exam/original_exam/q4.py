# write a program to check the given list is a palindrome

def is_palindrome(lst):
    return lst==lst[::-1]

input_lst=[1, 2, 3, 2, 1]
print(is_palindrome(input_lst))
