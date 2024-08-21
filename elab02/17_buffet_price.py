buffets = {
    'Japanese': 1000,
    'Korean': 1500
}

buffet = input("Enter your buffet choice: ")
if buffet in buffets:
    isWednesday = input("Is today Wednesday (yes/no)? ")
    if isWednesday == 'yes':
        print(f"Your payment is {buffets[buffet] * 0.85:.2f} Baht.")
    else:
        print(f"Your payment is {buffets[buffet]:.2f} Baht.")
else:
    print(f"Sorry, there is no {buffet} buffet.")
