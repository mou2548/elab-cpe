def count_digits(number):
  count = 0
  num = abs(number)
  while num > 0:
      num //= 10
      count += 1
  return count


def get_last_digit(n):
  """
  Get last digit in number
  :params number is an integer
  :return last digit in number
  
  >>> get_last_digit(41)
  1
  >>> get_last_digit(394)
  4
  >>> get_last_digit(1020)
  0
  """
  
  return n % 10


def get_distribution(number):
  """
  Return string showing distribution of number
  :params number (int): a number to find distribution
  :return string
  >>> get_distribution(21)
  '1x10^0 + 2x10^1'
  >>> get_distribution(306)
  '6x10^0 + 0x10^1 + 3x10^2'
  >>> get_distribution(12201)
  '1x10^0 + 0x10^1 + 2x10^2 + 2x10^3 + 1x10^4'
  """
  
  n = number
  distribution = ""
  for i in range(count_digits(n)):
      distribution += str(get_last_digit(n)) + 'x10^' + str(i) + " + "
      n //= 10
  return distribution

# Main
number = int(input("Input number: "))
distribution = get_distribution(number)
print(f"{number} = {distribution[:-3]}")
