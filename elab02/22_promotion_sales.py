discount = 0.95
total = 0
days = int(input("How many day : "))
for i in range(days):
    price = float(input(f"Input price in day {i+1} : "))
    price *= discount
    total += price
    discount -= 0.01

print(f"Summary price = {total:.2f}")
