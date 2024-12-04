from json import load

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\empoloyee.json")

data=load(f)

for emp in data:
    print(emp)