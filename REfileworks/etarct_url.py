from re import findall
f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\sampletext.txt")

content=f.read()

pattern="https?://[\w\S./]+"

URLS=findall(pattern,content)

for url in URLS:

        print(url)
