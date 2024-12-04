
from re import finditer

text="fatcatrunsveryfasttocathterat"

matcher=finditer("cat",text)#finditear(pattern,text)-->[(start,group),(),()]
for obj in matcher:

    print(obj.start(),obj.group())


