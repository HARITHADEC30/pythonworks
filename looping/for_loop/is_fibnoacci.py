numer=int(input("enter the number"))

prev=0
current=1
is_fibo=False

for i in range(1,numer+1):
    
    next=prev+current
 
    prev=current
    current=next
    if next==numer:
        is_fibo=True
        break
print(is_fibo)
