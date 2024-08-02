grid_size = [int(i) for i in input("Grid Size: ").split()]
mines_amount = int(input("Number of mine(s): "))
mines = []
for i in range(mines_amount):
    mines.append([int(i) for i in input(f"Mine#{i+1}: ").split()])

squares = []
for row in range(grid_size[1]):
    temp = [0] * grid_size[0]
    for mine in mines:
        if mine[1] == row:
            temp[mine[0]] = "X"
    squares.append(temp)

for row in range(grid_size[1]):
    for col in range(grid_size[0]):
        if squares[row][col] == "X":
            for i in range(-1, 2):
                if row+i < 0 or row+i >= grid_size[1]:
                    continue
                for j in range(-1, 2):
                    if col+j < 0 or col+j >= grid_size[0]:
                        continue
                    if squares[row+i][col+j] != "X":
                        squares[row+i][col+j] += 1

for row in squares:
    for spot in row:
        print(spot, end=" ")
    print()
        

