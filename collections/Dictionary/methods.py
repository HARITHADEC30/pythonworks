#---->.get(key)

employee={"id":1000,"name":"Sruthy","department":"Teacher","age":25,"salary":30000}

print(employee.get("department"))#get(key)
#invalid key return none

#----->pop(key) remove
employee.pop("salary")

print(employee)

#---->.keys()
#return all keys
for k in employee.keys():
    print(k)

#---->values()
#fetch all value 

for v in employee.values():
    print(v)

#---->items()
#fetch keys and values
for k,v in employee.items():
    print(k,v)
