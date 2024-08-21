def eat(S, P, G):
  dog = S
  paun = dog//P
  dog -= paun * P
  gane = dog//G
  dog -= gane * G
  return (paun, gane, dog)

S = int(input("Input starting food (S): "))
P = int(input("Input Paun's eating rate (P): "))
G = int(input("Input Gane's eating rate (G): "))
result = eat(S, P, G)
print(f"Paun eats {result[0]} time(s)")
print(f"Gane eats {result[1]} time(s)")
print(f"Remaining {result[2]} for dog")
