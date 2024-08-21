N = int(input("N: "))
M = int(input("M: "))
modulos = {}
for i in range(N):
    num = int(input(f"Input number {i+1}: "))
    modulos[num % M] = 1

print(len(modulos))