money = int(input("Enter initial amount in Baht: "))
interest = int(input("Enter interest rate in percent: "))

years = [1, 5, 10, 20]
for year in years:
    temp = money * (interest/100 + 1) ** year
    if (year > 1):
        print(f"Total amount after {year} years is {temp:.2f} Baht.")
    else:
        print(f"Total amount after {year} year is {temp:.2f} Baht.")
