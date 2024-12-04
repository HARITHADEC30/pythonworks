#create file reference
#in windows one \ is not acceptable so change \--->\\
#select one \ the click ctrl+d again and again 

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\students.txt","r")

for line in f:
    print(line)