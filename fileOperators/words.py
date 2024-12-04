f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\words.txt","r")

f_palindrome=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\palindrome.txt","w")

for line in f:

    word=line.rstrip("\n") 
    reversed_string=word[::-1]
    if reversed_string==word:
        f_palindrome.write(word+"\n")

f.close()
f_palindrome.close()

    




    