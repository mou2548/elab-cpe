weight = int(input("Weight: "))
height = int(input("Height: "))
bmi = weight / (height / 100) ** 2
if bmi >= 30:
    result = 'obese'
elif bmi >= 25 and bmi < 30:
    result = 'overweight'
elif bmi >= 18.6 and bmi < 25:
    result = 'healthy weight'
elif bmi < 18.6:
    result = 'underweight'

print(f"Your BMI is {bmi:.1f} You're in the {result} range.")
