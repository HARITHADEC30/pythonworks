#text=hello world
#  f=open("names.txt","w") 
# to write a file
#  f.write() 
# f.colse()
#argument must e str

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\names.txt","w")

languages=["python","java","javascript","c"]

for l in languages:

    f.write(l+"\n")

f.close()