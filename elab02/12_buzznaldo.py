time = int(input("How long have Buzz played ?: "))
hours = time // 60
if time % 60 > 20:
    hours += 1

price = 900 * hours
if hours >= 2 and hours < 4:
    price *= (1 - 0.1)
elif hours == 4:
    price *= (1 - 0.2)
elif hours >= 5:
    price *= (1 - 0.3)
print(f"Total price is {price:.0f} baht.")
