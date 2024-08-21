minutes = float(input("Minutes before due: "))
temperature = float(input("Temperature: "))
isRain = input("Is it raining (y/n)? ").lower()
days = (minutes / 60) / 24
if days < 1:
    days = round(days+0.5, 0)
else:
    days = round(days, 0)

print(f">>> {days:.0f} days before due.")
if days < 2:
    print(">>> I will do the assignment.")
elif days >= 2 and days <= 5:
    if temperature > 40 or (temperature > 25 and isRain == 'y'):
        print(">>> I will not do the assignment.")
    else:
        print(">>> I will do the assignment.")
elif days > 5:
    print(">>> I will not do the assignment.")
