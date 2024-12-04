f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

#for list
fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

    
print(fruits)

