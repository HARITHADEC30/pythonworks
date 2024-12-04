num1=int(input("enter number="))
num2=int(input("enter numer="))

try:#doubtful code
    result=num1/num2
    print(result)
# for the reason of error get
except Exception as e:
    print(e)

finally:
    print("file write")
    print("database commit")



