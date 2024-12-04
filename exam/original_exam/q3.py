# Write a python program to check parenthesis are valid
#         sample input : {}
#         sample output : valid
#         sample input : {[]}
#         sample output : valid
#         sample input : {([)}
#         sample output : invalid

user_input=input("enter the symbol")

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

    else:
        is_valid=False

if len(symbol_stack)==0 and is_valid==True:
    print("valid")
else:
    print("invalid")


