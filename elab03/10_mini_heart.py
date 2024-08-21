import math

def MiniHeart(x):
  return x*x + math.pi * (x/2)**2

L = float(input("Please enter the value of L: "))
area = MiniHeart(L)
print(f"Area is {area:.4f}")
