f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\test2.txt","a")

frameworks=["springboot","oodo","wordpress"]

for fw in frameworks:

    f.write(fw+"\n")

f.close()

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\test2.txt")

for fw in f:

    print(fw)

f.close()