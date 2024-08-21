if input("Is Bulotelli injured?(y/n) ") == 'y':
    print("Not available")
else:
    if input("Is Bulotelli late for the training?(y/n) ") == 'n':
        print("Starter")
    else:
        if input("Did Bulotelli perform well in training?(y/n) ") == 'y':
            print("Substitute")
        else:
            print("Not selected")
