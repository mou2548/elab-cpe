def plus(total,value):
    return total + int(value)

def minus(total, value):
    return total - int(value)

total = 0
n = int(input("How many food you have : "))
for i in range(n):
    food = input().split()
    if food[1] == '1':
        total = plus(total, food[0])
    elif food[1] == '-1':
        total = minus(total, food[0])
print(total)
