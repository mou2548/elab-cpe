n = int(input("Enter the number of rows or columns : "))
for i in range(1, n+1):
    for j in range(i, i+n):
        print('%2d ' % j, end="")
    print()