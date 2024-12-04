from re import finditer
text="I have 3 cars,2 bikes and 1-cycle"
#pattern="[ab]"#either a or b
#pattern="[a-z]" #check for all lowercase alphabets
#pattern="[a-zA-Z]" #check for all lowercase and uppercase alphabets
#pattern="[0-9]"#CHECK DIGITS
#pattern="[a-zA-Z0-9]"#CHECK DIGITS & ALPHABETS
#pattern="[^ak]"#exclude a and k

pattern="\w"   #[a-zA-Z0-9] for getting alphanumeric another method
pattern="\d"   #"[0-9]" to get digits 
pattern="\D"   #Exclude digits
pattern="\W"   #exclude alphanumeric or get special character
pattern="\s"   #get space
pattern="\S"   #exclude space
#all lower case alphabets exclude a&k
#pattern="[^ak, A-Z0-9]"
#pattern="[^A-Za-z0-9]"#check special charcter
#for remove -  "[/-]"
matcher=finditer(pattern,text)

for obj in matcher:
    print(obj.start(),"==>",obj.group())#[(start=4,group=a),[start=11, group=a),stat=17,gruop=b]
              #position         #group GIVE AS TUPLE
              