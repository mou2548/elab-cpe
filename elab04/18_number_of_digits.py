def count_digits(number):
   """
   Get number of digits in number
   :params number is an integer
   :return number of digits in number
   >>> count_digits(41)
   2
   >>> count_digits(-41)
   2
   >>> count_digits(1)
   1
   """
  
  count = 0
  num = abs(number)
  if num == 0:
     return 1
    
  while num > 0:
    num //= 10
    count += 1
  return count

# Main
number = int(input("Enter number: "))
print(f"There are {count_digits(number)} digits in {number}")
