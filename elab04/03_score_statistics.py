scores = []
while True:
    score = input("Enter student score (or just ENTER to finish): ")
    if len(score) == 0:
        break
    scores.append(int(score))
    
for i in range(len(scores)):
    print(f"Score #{i+1}: {scores[i]}")

print(f"Average score is {sum(scores) / len(scores):.2f}")
print(f"Minimum score is {min(scores)}")
print(f"Maximum score is {max(scores)}")
