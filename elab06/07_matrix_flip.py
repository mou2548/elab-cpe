direction = input("Direction to flip square (V/H): ")
size = int(input("Input size of square: "))

square = []
for i in range(size):
    square.append(input().split())

print("After flip:")
if direction == 'V':
    for i in range(size-1, -1, -1):
        for num in square[i]:
            print(num, end=" ")
        print()
elif direction == 'H':
    for i in range(0, size):
        for j in range(size-1, -1, -1):
            print(square[i][j], end=" ")
        print()