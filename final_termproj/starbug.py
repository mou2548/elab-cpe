def readMenu(fn='CoffeeMenu01.txt'):
    with open(fn) as fd:
        return fd.read()

class CupOfCoffee():
    
    def __init__(self, coffee_type='Espresso', drinking_type='Hot', price=0):
        self.coffee_type = coffee_type
        self.drinking_type = drinking_type
        self.price = price
        self.add_on = ["no"]

    def set_add_on(self, one_add_on, one_add_on_price):
        if "no" in self.add_on:
            self.add_on = []
        self.add_on.append(one_add_on)
        self.price += one_add_on_price
    
    def __repr__(self):
        if "no" in self.add_on:
            txt = 'no add on'
        elif len(self.add_on) == 1:
            txt = f'{self.add_on[0]}'
        else:
            txt = f'{", ".join(self.add_on[:-1])} and {self.add_on[-1]}'
        return f" This cup is {self.drinking_type.lower()} {self.coffee_type} with {txt}, {self.price} baht."

class CustomerBill():
    
    def __init__(self, name='Patiphat'):
        self.name = name
        self.ordered_coffee = []

    def add_ordered_coffee(self, aCupOfCoffeeObject):
        self.ordered_coffee.append(aCupOfCoffeeObject)

    def receipt(self):
        total = 0
        strings = '++++++++++++++++++++++++++++++++\n'
        strings += f'{"CPE38 **StarBUG Cafe":^32}\n'
        txt = f"Kun {self.name}'s Receipt"
        strings += f"{txt:^32}\n"
        strings += '++++++++++++++++++++++++++++++++\n'
        strings += f'{"Description":<27}{"Price":>5}\n'
        for coffee in self.ordered_coffee:
            total += coffee.price
            coffee_name = f'{coffee.drinking_type} {coffee.coffee_type}'
            strings += (f'{coffee_name:<27}{coffee.price:>5}\n')
            for add_on in coffee.add_on:
                if "no" in add_on:
                    break
                strings += f' + {add_on}\n'
            strings += '\n'
        strings += f'{"Total":<27}{total:>5,}\n'
        strings += '++++++++++++++++++++++++++++++++\n'
        strings += f'{"Thank you, please come back :)":^32}\n'
        strings += '++++++++++++++++++++++++++++++++\n'

        return strings

def parseMenu(menu_csv):
    return [
        [data[0]] + list(map(int, data[1:])) 
        for data in (menu.strip().split(',') for menu in menu_csv.split('\n') if menu and menu != ' ')
    ]

def printMenu(coffee_menu, add_on_menu):
    print("Welcome to CPE38 **StarBUG Cafe!")
    print("+++++++++++++ MENU +++++++++++++")
    print(f"{'Coffee':<13}  {'Hot':>3}  {'Cold':>4}  {'Frappe'}")
    for i, coffee in enumerate(coffee_menu, 1):
        print(f"{i}.{coffee[0]:<13}{coffee[1]:>3}  {coffee[2]:>4}  {coffee[3]:>4}")
    print("++++++++++++ ADD-ON ++++++++++++")
    for i, add_on in enumerate(add_on_menu, 1):
        print(f"{i}.{add_on[0]:<20}{add_on[1]:>2}")
    print("++++++++++++++++++++++++++++++++")
    print()

def checkInput(Input, max=None):
    try:
        Input = int(Input)
        if max == None or (0 < Input <= max):
            return True
    except:
        return False
    return False

def customerOrder(customer, coffee_menu, add_on_menu):
    DRINK_TYPE = ['H', 'C', 'F']
    drinking_type_shorthand = {'H': 'Hot', 'C': 'Cold', 'F':'Frappe'}
    
    while True:
        cups = input("How many cups of coffee to order? ")
        if not checkInput(cups):
            print(" ERROR: Invalid input!")
            continue
        cups = int(cups)
        break

    for i in range(1, cups+1):
        while True:
            coffee_num = input(f"Cup #{i}, please select type of coffee: ")
            if not checkInput(coffee_num, len(coffee_menu)):
                print(" ERROR: Invalid input!")
                continue
            coffee_num = int(coffee_num)
            coffee = coffee_menu[coffee_num-1]
            coffee_type = coffee[0]
            break
        
        drink_available = []
        for pos, price in enumerate(coffee[1:]):
            if price != 0:
                drink_available.append(DRINK_TYPE[pos])
        
        drinking_type = drink_available[0]
        drinking_num = DRINK_TYPE.index(drinking_type)
        while len(drink_available) > 1:
            txt = ','.join(drink_available)
            drinking_type = input(f"Cup #{i}, please select drinking type ({txt}): ").upper()
            if drinking_type not in drink_available:
                print(" ERROR: Invalid input!")
                continue
            drinking_num = DRINK_TYPE.index(drinking_type)
            break

        drinking_type = drinking_type_shorthand[drinking_type]
        price = coffee[drinking_num+1]
        Coffee = CupOfCoffee(coffee_type, drinking_type, price)
        add_ons = []
        while len(add_ons) < len(add_on_menu):
            add_on_num = input(f"Cup #{i}, please select add on (enter for exit): ")
            if add_on_num == '':
                break
            if not checkInput(add_on_num, len(add_on_menu)) or add_on_num in add_ons:
                print(" ERROR: Invalid input!")
                continue
            add_ons.append(add_on_num)
            add_on_num = int(add_on_num)
            add_on_name, add_on_price = add_on_menu[add_on_num-1]
            Coffee.set_add_on(add_on_name, add_on_price)
        print(Coffee)
        customer.add_ordered_coffee(Coffee)

def generateDict(coffee_menu):
    coffee_dict = {}
    for coffee in coffee_menu:
        coffee_dict[coffee[0]] = 0
    return coffee_dict

def generateReport(coffee_dict, totalSold):
    strings = '++++++++++++++++++++++++++++++++\n'
    strings += f'{"CPE38 **StarBUG Cafe":^32}\n'
    strings += f'{"Report for Coffee sold today":^32}\n'
    strings += '++++++++++++++++++++++++++++++++\n'
    for key, value in coffee_dict.items():
        if value > 0:
            strings += f' {key:<24}{value} cup'
            if value > 1:
                strings += 's'
            strings += '\n'
    strings += f'\nTotal sold amount{totalSold:>10,} baht\n'
    strings += '++++++++++++++++++++++++++++++++\n'
    txt = "What's a good day!"
    strings += f'{txt:^32}\n'
    strings += '++++++++++++++++++++++++++++++++\n'

    return strings

def runStarBUGcafe_main():
    coffee_menu, add_on_menu = parseMenu(coffee_menu_CSV), parseMenu(add_on_menu_CSV)
    totalSold, coffee_dict = 0, generateDict(coffee_menu)
    while True:
        printMenu(coffee_menu, add_on_menu)
        name = input("Enter customer's name: ")
        if name == 'Good Day':
            break
        customer = CustomerBill(name)
        customerOrder(customer, coffee_menu, add_on_menu)
        for coffee in customer.ordered_coffee:
            totalSold += coffee.price
            coffee_dict[coffee.coffee_type] += 1
        print(customer.receipt())
    print(generateReport(coffee_dict, totalSold))

coffee_menu_filename = input('Enter Coffee Menu available today (filename): ')
coffee_menu_CSV = readMenu(coffee_menu_filename)
addon_menu_filename = input('Enter AddOn Menu available today (filename): ')
add_on_menu_CSV = readMenu(addon_menu_filename)

runStarBUGcafe_main()