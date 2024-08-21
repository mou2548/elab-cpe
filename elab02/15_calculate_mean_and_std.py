name = ['a', 'b', 'c', 'd', 'e']
List = []
mean = 0
sd = 0
for i in range(5):
    temp = int(input(f"Input {name[i]}: "))
    mean += temp
    List.append(temp)
mean /= 5

for i in range(5):
    sd += (List[i] - mean) ** 2
sd = (sd/5)**0.5
print(f"mean: {mean:.3f}")
print(f"sd: {sd:.3f}")
