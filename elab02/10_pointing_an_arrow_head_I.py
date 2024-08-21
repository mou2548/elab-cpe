num = int(input("Input number: "))
while num % 2 == 0:
    print("Please input odd number")
    num = int(input("Input number: "))

for i in range(num):
    print('x' * (i+1))
for i in range(num - 1, 0, -1):
    print('x' * i)
