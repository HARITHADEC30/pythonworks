num1=int(input("enter number="))
num2=int(input("enter numer="))

try:#doubtful code
    result=num1/num2
    print(result)

except Exception as e:#error handling
    num2=int(input("enter number2="))#throug another way the error will be handeled
    result=num1/num2
    print(e)

finally:
    print("file write")
    print("database commit")