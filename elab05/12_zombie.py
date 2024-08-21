people = []
time_left = []
time = 0
n, m = [int(i) for i in input().split()]
for i in range(n):
    temp = int(input())
    people.append(temp)
    time_left.append(temp)

min_time = min(people)
while m > 0:
    time += 1
    for i in range(n):
        time_left[i] -= 1
        if time_left[i] <= 0:
            m -= 1
            time_left[i] += people[i]
print(time)
