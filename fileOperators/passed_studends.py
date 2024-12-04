f1=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\all_studends.txt","r")
f2=open("C:\\Users\\Sruthy\\Desktop\\pythonworks\\datasets\\failed.txt","r")
all_studends_set=set()
failed_students_set=set()


for line in f1:
    line=line.rstrip("\n")
    all_studends_set.add(line)

for line in f2:
    line=line.rstrip("\n")
    failed_students_set.add(line)

passed_studends=all_studends_set.difference(failed_students_set)
print(passed_studends)
    