scores = []
while True:
    score = input("Enter student score (or just ENTER to finish): ")
    if len(score) == 0:
        break
    scores.append(int(score))

scores.sort(reverse=True)
for i in range(len(scores)):
    print(f"Rank #{i+1}: {scores[i]}")
