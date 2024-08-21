months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
d = int(input("d: "))
m = int(input("m: "))
y = int(input("y: "))

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    months[1] += 1

total = d
if m > 1:
    total += sum(months[0:m-1])
print(total)
