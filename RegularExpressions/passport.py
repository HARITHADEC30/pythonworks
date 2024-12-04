# First character: An uppercase alphabet
# Second and third characters: Two numbers, with the first ranging from 1 to 9 and the second from 0 to 9
# Fourth through seventh characters: Any number from 0 to 9
# Last character: Any number from 1 to 9
# White space: Zero or one white space character may be included

from re import fullmatch

passport_number=input("enter the number=")

pattern="[A-Z][1-9][0-9]\d{4}[1-9]\s?"

matcher=fullmatch(pattern,passport_number)

if matcher==None:
    print("invalid")

else:
    print("valid")