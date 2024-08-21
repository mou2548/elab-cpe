positive, negative = 0, 0
while True:
    num = float(input("Enter a number (to exit, just enter 0): "))
    if num == 0:
        break
    if num > 0:
        positive += num
    else:
        negative += num

print(f"The sum of positive numbers is {positive:.2f}")
print(f"The sum of negative numbers is {negative:.2f}")
