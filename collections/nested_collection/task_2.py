student_data={
    "hari":[45,40,35],
    "vipin":[34,40,45],
    "vinay":[45,40,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}

# index=1 hari's avg mark
# inde=5 anvin's avg mark
index=1
for i,element in enumerate(student_data):
    if i+1 == index:
        print(element)
        mark=student_data.get(element)
        avg=sum(mark)/len(mark)
        print(avg)

index=5
for i,element in enumerate(student_data):
    if i+1 == index:
        print(element)
        mark=student_data.get(element)
        avg=sum(mark)/len(mark)
        print(avg)



# #for index:avg
# student_avg={k:sum(v)/len(v) for k,v in student_data.items()}
# print(student_avg)
   



source_word="REGULATE"

target_word="LATTER"

#kangaroo_word

source_word.split()
target_word.split()
