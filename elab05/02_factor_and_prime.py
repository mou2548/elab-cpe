def list_factors(n):
    """
    Get string of factors of n
    :params n is an integer to find factors
    :return string of factors (with a space between each factor)
    >>> list_factors(6)
    '1 2 3 6 '
    >>> list_factors(7)
    '1 7 '
    >>> list_factors(12)
    '1 2 3 4 6 12 '
    """
    string_factors = ''
    for i in range(1, n+1):
        if n % i == 0:
            string_factors += str(i) + ' '
    return string_factors

def find_sum_and_num_factors(n):
    """
    Find summation and count number of factors of n
    :params n is an integer to find factors
    :return sum is summation of factors of n
            count is number of factors of n
    >>> find_sum_and_num_factors(6)
    (12, 4)
    >>> find_sum_and_num_factors(7)
    (8, 2)
    >>> find_sum_and_num_factors(12)
    (28, 6)
    """
   
    List = [int(i) for i in list_factors(n).split()]
    return (sum(List), len(List))

num = int(input("Enter positive number: "))
print(f"Factors of {num} are")
print(list_factors(num))
print(f"Sum of {list_factors(num)}is {find_sum_and_num_factors(num)[0]}")
print(f"Number of factors is {find_sum_and_num_factors(num)[1]}")

isPrime = True
if num == 1:
   isPrime = False
   
for i in range(2, round(num**0.5)+1):
   if num % i == 0:
      isPrime = False
if isPrime:
   print(f"{num} is prime number.")
else:
   print(f"{num} is not prime number.")

