#crate dictionary employee with keys eid,name,salary,department,eperiense

employee={"eid":1000,
         "name":"najiya",
         "salary":100000,
         "department":"developer",
         "eperiense":6}

print(employee["salary"])

#add contact as 345678

employee["contact"]=345678
print(employee)

# if experience >5 update empoyee salary as current_slary+10000
#else cureent_salary+5000

if employee["salary"]>5:

    employee["salary"]+=10000

else:
    employee["salary"]-=5000

print(employee)

#add role as SDE IF EXP> 5 ELSE add role as JDE

if employee["eperiense"]>5:
    employee["role"]="SDE"

else:
    employee["role"]="JDE"

print(employee)
