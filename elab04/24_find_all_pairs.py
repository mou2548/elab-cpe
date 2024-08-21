List = [int(num) for num in input("Enter list of number: ").split()]
answer = []

for i in range(len(List)):
    for j in range(i+1, len(List)):
        if abs(List[i]-List[j]) == 3:
            pair = [List[i], List[j]]
            answer.append(pair)

print("Output list:", answer)
