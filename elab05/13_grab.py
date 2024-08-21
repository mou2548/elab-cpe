total = 0
group = []
for num in input().split():
    group.append(int(num))
    if 4 in group:
        group.remove(4)
        total += 1
    elif 1 in group and 3 in group:
        group.remove(1)
        group.remove(3)
        total += 1
    elif group.count(2) == 2:
        group.remove(2)
        group.remove(2)
        total += 1

group_sum = sum(group)
while group_sum > 0:
    group_sum -= 4
    total += 1

print(total)