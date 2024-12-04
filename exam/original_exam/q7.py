# Given a string, write a Python program to find and print the longest palindromic
# substring within the string. A palindrome is a word that reads the same forward
# and backward.The substring should be contiguous

# Input:
# s = "racecar"
# longest_palindromic_substring(s)
# Output:
# racecar
def longest_palindromic_substring(s: str) -> str:
    longest = ""
    
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            
            # Check if the substring is a palindrome
            if substring == substring[::-1]:
                # Update longest if this palindrome is longer
                if len(substring) > len(longest):
                    longest = substring
    
    return longest

s = "racecar"
print(longest_palindromic_substring(s)) 