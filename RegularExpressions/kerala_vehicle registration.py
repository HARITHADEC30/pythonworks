#starting with kl

#2 digits

#alphabets minimum 1 maximum 2
#4 digit

from re import fullmatch

user_input=input("enter the number=")

pattern="(KL|kl)[0-9]{2}[A-Z]{1,2}[0-9]{4}" # ? optional varam varandirikkam   
                                             #(kl|KL) MEANS OR
                         # + should be present for one time 
matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
else:
    print("valid")


    #PASSPORT
    #ADHAR NUMBER
    #DRIVING LICENSE NUMBER