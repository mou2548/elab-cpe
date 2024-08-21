def calculate(x, case, y):
    if case == '+':
        return x + y
    elif case == '-':
        return x - y
    elif case == '*':
        return x * y
    elif case == '/':
        return format(x / y, '.2f')
    elif case == '%':
        return x % y
    else:
        return "Unknown Operator"

x = int(input("x: "))
operator = input("Operator: ")
y = int(input("y: "))
print(calculate(x, operator, y))
