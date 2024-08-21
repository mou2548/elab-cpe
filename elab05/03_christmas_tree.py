levels = int(input("Enter number of levels: "))
bush = int(input("How big is each bush? "))

for level in range(levels):
    for i in range(bush):
        print(' ' * (bush-1-i) + '*' * (2*i+1))