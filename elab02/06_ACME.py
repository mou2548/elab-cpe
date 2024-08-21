amount = float(input("Enter buying amount: "))
if amount >= 1000 and amount < 3000:
    amount *= (1 - 0.1)
elif amount >= 3000:
    amount *= (1 - 0.15)
print(f"Amount due after discount is {amount:.2f} baht.")
