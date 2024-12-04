def romanToDecimal(roman):
    roman_values={
        "I":1,"V":5,"X":10,"L":50, "C":100, "D":500, "M":1000
    }
    result=0
    for i in range(len(roman)):
        v1=roman_values.get(roman[i])
        if i+1 < len(roman):
            v2=roman_values.get(roman[i+1])
            if v1>=v2:
                result+=v1
            else:
                result-=v1
        else:
            result+=v1

    return result

roman=input("Enter the Roman value :").upper()
print(romanToDecimal(roman))