List = [int(i) for i in input().split()]

while True:
    menu, x = input().split()
    x = int(x)

    if menu == 'A':
        List.append(x)
    elif menu == 'S':
        print(List[x])
    elif menu == 'R':
        List.pop(x)
    elif menu == 'E':
        for i in List:
            print(i, end=" ")
        break