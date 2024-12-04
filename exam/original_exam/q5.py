# read user weight in kg,height in cm,gender
# calculate BMI (weight_in_kg/(height_in_meter**2))
# bmi<19 display Underweight
# 19-bmi-25 display normal weight
# 25-bmi-30 display overweight
# bmi>30 display obese

weight_in_kg=int(input("enter weight="))
height_in_meter=int(input("enter height="))

bmi=weight_in_kg/(height_in_meter**2)

print(bmi)
if bmi<19:
    print("underwight")

elif 19<bmi<25:
    print("normla")