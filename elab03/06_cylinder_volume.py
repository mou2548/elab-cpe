import math

def find_cylinder_volume(h, r):
  return math.pi * h * r**2

r = float(input("radius = "))
h = float(input("height = "))
V = find_cylinder_volume(h, r)

print(f"Volume = {V:.2f}")
