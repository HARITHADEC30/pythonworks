#----->add()
arr=[10,10,20,30,40,50,40]

st=set()#uniqu elements
#fetch numbers from array
for i in arr:
    #add num to set
    st.add(i)
#display set
print(st)


# ------>intersection()

st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)#----commen elements from two sets

print(intersection_set)


#------>union()

union_set=st1.union(st2)

print(union_set)#----all elements from two sets and not duplicates

#------>difference()

difference_set=st1.difference(st2)

print(difference_set)#----differense= set 1 without elemnts from set2


#------>remove()

s1={10,20,30,40,50}
st.remove(50)
print(st)

#----->issubset

st1={1,2,3}
st2={1,2,3,4,5}

print(st1.issubset(st2))#True

#---->issuperset
# set of elemnts containing all of the elemts of another set
print(st2.issuperset(st1))

#----->symmetric_difference()

set1={1,2,3,10,20}
set2={1,2,3,4,5}

#10,20,4,5
syymetric_diffrence=set1.symmetric_difference(set2)

print(syymetric_diffrence)


#------>update()

set1.update(set2)#mutable

print(set1)