f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\framework.txt","a")
framework=["wordpress","springboot","oodo","fastapi"]

for fw in framework:
    f.write(fw+"\n")

f.close()
