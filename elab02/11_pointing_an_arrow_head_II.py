string = input("Enter a string: ")
size = int(input("Enter arrow's size (greater than 0): "))

if size <= 0:
    print("Size must be greater than 0.")
elif size % 2 == 0:
    for i in range(size // 2):
        print(' ' * i + string)
    for i in range(size // 2 - 1, -1, -1):
        print(' ' * (i) + string)
else:
    for i in range(size // 2):
        print(' ' * i + string)
    for i in range(size // 2, -1, -1):
        print(' ' * (i) + string)
