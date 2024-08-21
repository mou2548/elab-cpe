lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("Enter text: ")
step = int(input("Enter step: "))
for letter in text:
    if letter.isalpha(): 
        if letter.islower():
            letter = lower[((ord(letter) - 97) + step) % 26]
        else:
            letter = upper[((ord(letter) - 65) + step) % 26]
    print(letter, end="")
