from re import findall
f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\dates.txt")

content=f.read()

pattern="[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:

        print(date)


#scrapping
#beutyfullsoup is the site for scrapping