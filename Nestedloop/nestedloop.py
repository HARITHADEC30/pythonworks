print("good",end="**")
print("afternoon", end= "\t")
print("all")

for row in range(1,5):
    for col in range(1,6):
        print("*",end="\t")
    print()        


#  c1  c2  c3  c4
#1  *   *   *   *
#2  *   *   *   *
#3  *   *   *   *
#4  *   *   *   *

for row in range(1,5):
    for col in range(1,4):
        print("*",end="\t")
    print()