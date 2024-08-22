class Coin:
    def __init__(self, value = 1):
        self.value = value

    def __str__(self):
       return f'{self.value} Baht Coin'

class BankNote:
    def __init__(self, value = 20):
        self.value = value

    def __str__(self):
        return f'{self.value} Baht Banknote'

bag = {}
amount = int(input("Input amount : "))

banks = [1000, 500, 100, 50, 20]
coins = [10, 5, 2, 1]
if amount > 0:
    for money in banks+coins:
        if amount // money > 0:
            bag[str(money)] = amount // money
            amount %= money

for key, value in bag.items():
    key = int(key)
    if key in banks:
        string = BankNote(key)
    else:
        string = Coin(key)
    print(f"You get {value} of {string}")
        
