def factorial(x): 
  fac_sum = 1
  for i in range(1, x+1):
      fac_sum *= i
  return fac_sum


k = int(input("Input k: "))
total = 0
for i in range(1, k+1):
    fac = factorial(i)
    total += fac
    print(f"{i}! = {fac}")

print(f"Summation of factorial 1!-{k}! = {total}")
