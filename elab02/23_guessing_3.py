guess = 0
while guess != target:
    guess = int(input("Enter your guess (0 - 100): "))
    if guess < 0 or guess > 100:
        print("Sorry, out of range, try again later.")
    elif guess > target:
        print("Sorry, your guess is too high, try again later.")
    elif guess < target:
        print("Sorry, your guess is too low, try again later.")

print("Congratulations, your guess is correct.")
