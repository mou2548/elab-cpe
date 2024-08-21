lucky_number = input("Enter lucky number : ")
candidates_amount = int(input("Enter amount of candidates : "))

winner = 0
highest = 0

for i in range(candidates_amount):
    id = input(f"Enter ID card number {i+1}: ")
    count = id.count(lucky_number)
    if count > highest or (count == highest and int(id) > int(winner)):
        winner = id
        highest = count

print("Winner:", winner)
