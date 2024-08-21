string = input("Enter list of words: ").replace(" ", "")
print(sum(1 for c in string if c.islower()))
