sentence = input("Input sentence: ")
rows = int(input("Input row: "))
answer = [[] for i in range(rows)]

row = [i for i in range(rows)]
for i in range(rows-2, 0, -1):
    row.append(i)

for i in range(len(sentence)):
    answer[row[i % len(row)]].append(sentence[i])

for row in answer:
    for c in row:
        print(c, end="")
print()