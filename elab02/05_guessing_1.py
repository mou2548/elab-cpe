guess = int(input("Enter your guess (0 - 100): "))
if guess < 0 or guess > 100:
    print("Sorry, out of range, try again later.")
elif guess == target:
    print("Congratulations, your guess is correct.")
else:
    print("Sorry, your guess is wrong, try again later.")
