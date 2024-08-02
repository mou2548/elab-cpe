GRID_SIZE = [8, 8]

row = int(input("Enter Rook's row position: "))
col = int(input("Enter Rook's column position: "))

for i in range(GRID_SIZE[1] * 2 + 1):
    if i % 2 == 0:
        print('-' * (GRID_SIZE[1] * 2 + 1))
        continue
    for j in range(GRID_SIZE[0]):
        if i == row * 2 + 1 and j == col:
            print("|R", end="")
        elif i == row * 2 + 1 or j == col:
            print("|x", end="")
        else:
            print("| ", end="")
    print('|')
