
#BMI=weight in kg/(height in meter)**2
weight_in_kg = int(input("enter weight in kg :"))

height_in_cm = int(input("enter height in cm :"))

height_in_meter = height_in_cm / 100

BMI=weight_in_kg / (height_in_meter)**2

BMI = round(BMI,2)

print(BMI)
#print under weight if bmi<19
#print normal weight if bmi 19 to <25
#print overwight if bmi 25 to<30
#print oese if mi >=30
if BMI<19:
    prin("underweight")

elif BMI>=19 and BMI<25:
    print("normal")

# elif BMI>=25 and BMI<30:
#     print("overweight")

elif 25<=BMI<30:
    print("overweight")

elif BMI>30:
    print("obese")

else:
    print("invalid")