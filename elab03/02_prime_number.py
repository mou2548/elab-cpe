def check_prime(n):
    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
