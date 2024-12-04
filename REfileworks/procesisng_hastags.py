from re import finditer

f=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\social_post.txt")

for line in f:

    hastags=line.rstrip("\n")
    pattern="#\w+"

    matcher=finditer(pattern,hastags)

    for obj in matcher:

        print(obj.group())

       