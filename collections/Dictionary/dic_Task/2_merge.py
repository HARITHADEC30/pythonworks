#2. Write a Python program to merge two dictionaries.
dict1={"sneha":23,"haritha":21,"alphy":22,"sourav":23,"paru":22}
dict2={"rohith":23,"ahaari":21,"pooja":22,"sourav":23,"natasha":22}
# text={num1+num2 for num1 in dict1.items() for num2 in dict2.items()}
# merge=dict1|dict2
# print(merge)
dict1.update(dict2)
print(dict1)

