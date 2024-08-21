high = 0
high_num = 0
streak = 0
same = 0
x = -1
while x != 0:
    x = int(input())
    if x != same:
        streak = 0
    streak += 1
    if streak > high:
        high = streak
        high_num = x
    same = x
print(high)
print(high_num)
