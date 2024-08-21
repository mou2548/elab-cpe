age = int(input("Enter your age: "))
income = int(input("Enter your net income: "))

nit = 0
if age < 15 or age > 60:
    print("Invalid age.")
elif income < 1 or income > 79999:
    print("Invalid income.")
else:
    nit = 0.2 * income
    if income > 30000:
        nit = 0.2 * 30000
        nit -= 0.12 * (income - 30000)
    print(f"Your negative income tax is {nit:.2f} Baht.")
