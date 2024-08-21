age = int(input("Enter your age : "))

if age >= 0 and age <= 12:
    print("You are Child.")
elif age >= 13 and age <= 18:
    print("You are Adolescence.")
elif age >= 19 and age <= 59:
    print("You are Adult.")
elif age >= 60:
    print("You are Senior Adult.")
