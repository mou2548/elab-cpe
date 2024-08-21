isLeap = False

year = int(input("Enter year: "))
if year >= 1:
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            isLeap = True
    
    if isLeap:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
else:
    print("Invalid year.")
    
