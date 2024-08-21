products = {
    'TV': 6000,
    'DVD player': 1500,
    'Audio System': 3000
}

price = 0
discount = 0
for product in products.keys():
    price += int(input(f"How many {product}s? ")) * products[product]
print(f"Total price is {price:.2f} baht.")

if price >= 24000:
    discount = price * 0.2
    print(f"You've got a discount of {price * 0.2:.2f} baht.")

price -= discount
print(f"Your payment is {price:.2f} baht. Thank you!")
