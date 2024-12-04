from re import fullmatch

Date=input("enter the number=")

pattern="([1-9]|0[1-9]|1[0-2])"#month
        #"0?[1-9]|1[0-2]"
pattern="([1-9]|0[1-9]|1[0-9]|2[0-9]|3[01])"#date
pattern="0?[1-9]|[12][0-9]|3[01]"#more short 
#validate year from 1800-2024
      
pattern="(18[0-9]{2}|19[0-9]{2}|20[01][0-9]|202[0-4])"#
matcher=fullmatch(pattern,Date)

if matcher==None:
    print("invalid")

else:
    print("valid")
