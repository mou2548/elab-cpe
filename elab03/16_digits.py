def digit(n):
    return n % 10

def tens(n):
    return n % 100 // 10

def hundreds(n):
    return n % 1000 // 100

def thousands(n):
    return n // 1000

def sum_digits(n):
    return digit(n) + tens(n) + hundreds(n) + thousands(n)
