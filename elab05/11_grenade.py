def killCheck(row ,col):
    global kill
    for i in range(row-2, row+3):
        for j in range(col-2, col+3):
            if i < 0 or i > n-1 or j < 0 or j > n-1:
                continue
            if area[i][j] == 'E':
                kill += 1
                area[i][j] = 'D'

area = []
kill = 0

n = int(input())
for i in range(n):
    area.append(input().replace("", " ").split())

for i in range(n):
    for j in range(n):
        if area[i][j] == 'G':
            killCheck(i, j)
print(kill)