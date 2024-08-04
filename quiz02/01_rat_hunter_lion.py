def printAnimal(animal1, animal2):
    D = {
        '1': '__QQ\n()">'.split('\n'),
        '2': ' O \n/|\\\n/ \\'.split('\n'),
        '3': ' /\_/\ \n( o.o )\n > ^ < '.split('\n')
    }
    pic = (D[animal1], D[animal2])
    for i in range(max(len(pic[0]), len(pic[1]))):
        try:
            print(pic[0][i], end="  ")
        except:
            print(' ' * len(pic[0][0]), end="  ")
        if i == 1:
            print('VS', end="  ")
        else:
            print('  ', end="  ")
        try:
            print(pic[1][i], end="  ")
        except:
            print(' ' * len(pic[1][0]), end="  ")
        print()

p1_name = input("Player1 name: ")
p2_name = input("Player2 name: ")
p1_score = 0
p2_score = 0
match = 0

while match < 5:
    print()
    print(f"Round {match+1}!")
    print(f"{p1_name} {p1_score} / {p2_name} {p2_score}")
    p1_choice = (input(f"{p1_name}'s choice (1/rat, 2/hunter and 3/lion): "))
    p2_choice = (input(f"{p2_name}'s choice (1/rat, 2/hunter and 3/lion): "))

    printAnimal(p1_choice, p2_choice)
    
    if p1_choice == p2_choice:
        pass
    elif p1_choice == '1' and p2_choice == '2':
        p1_score += 1
    elif p1_choice == '2' and p2_choice == '3':
        p1_score += 1
    elif p1_choice == '3' and p2_choice == '1':
        p1_score += 1
    else:
        p2_score += 1

    if p1_score == 3:
        print()
        print(f"{p1_name} {p1_score} / {p2_name} {p2_score}")
        print(f"{p1_name} win!")
        print()
        break
    elif p2_score == 3:
        print()
        print(f"{p1_name} {p1_score} / {p2_name} {p2_score}")
        print(f"{p2_name} win!")
        print()
        break
    match += 1

if match == 5:
    print()
    print(f"{p1_name} {p1_score} / {p2_name} {p2_score}")
    print("Draw!")
    print()

    
