directions = {
    'N': 0,
    'S': 0,
    'E': 0,
    'W': 0
}

city_size = [int(i) for i in input("City Size: ").split()]

city = []
for row in range(city_size[0]):
    city.append([int(i) for i in input().split()])

# North
count = 0
for col in range(city_size[1]):
    now = city[0][col]
    count += 1
    for row in range(1, city_size[0]):
        if city[row][col] > now:
            count += 1
            now = city[row][col]
directions['N'] = count

# South
count = 0
for col in range(city_size[1]):
    now = city[city_size[0] - 1][col]
    count += 1
    for row in range(city_size[0] - 1, -1, -1):
        if city[row][col] > now:
            count += 1
            now = city[row][col]
directions['S'] = count


# East
count = 0
for row in range(city_size[0]):
    now = city[row][city_size[1] - 1]
    count += 1
    for col in range(city_size[1] - 1, -1, -1):
        if city[row][col] > now:
            count += 1
            now = city[row][col]
directions['E'] = count

# West
count = 0
for row in range(city_size[0]):
    now = city[row][0]
    count += 1
    for col in range(city_size[1]):
        if city[row][col] > now:
            count += 1
            now = city[row][col]
directions['W'] = count

most_view = max(directions.values())
for direction, value in directions.items():
    if value == most_view:
        print(direction, end=" ")
print()
