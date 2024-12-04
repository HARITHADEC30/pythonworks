#sample input="{}"
#output=valid

#sample input="{()}"
#output=valid

#sample input="{(})"
#output=invalid

# #sample input="[]("
#output=invalid
# importend qustion must come in exam
user_input=input("enter bracket pair")

bracket_pair={"[":"]","{":"}","(":")"}

symbol_stack=[]
top=-1
is_valid=True
for symbol in user_input:
    if symbol in bracket_pair:
        top=top+1
        symbol_stack.append(symbol)
    elif top==-1:
        is_valid=False
    elif symbol==bracket_pair.get(symbol_stack[top]):
        symbol_stack.pop()
        top=top-1
    else:
        is_valid=False

if len(symbol_stack)==0 and is_valid==True:
    print("valid")
else:
    print("invalid")
print(is_valid)
  

