text="ABABBCCDDE"

charcter_frequency={ch:text.count(ch) for ch in text}

print(charcter_frequency)

#print non recursive elemnts

non_recursive=[k for k,v in charcter_frequency.items() if v==1]

print(non_recursive)
# another method
for k,v in charcter_frequency.items():

    if v==1:

        print(k)
        print(max(charcter_frequency))