f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\sample.txt","w")

message=input("Write something:")

f.write(message+"\n")

f.close()

f_read=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\sample.txt")

for message in f_read:

    print(message)
    
f_read.close()