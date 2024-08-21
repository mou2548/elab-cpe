def calGrades(score):
    grades = {
        1.5:'A',
        1.0:'B+',
        0.5:'B',
        0.0:'C+',
        -0.5:'C',
        -1.0:'D+',
        -1.5:'D',
    }
    diff = score - avg
    for grade in grades.keys():
        if diff >= grade * sd:
            return grades[grade]
    return 'F'

scores = []
while True:
    score = input("Enter student score (or just ENTER to finish): ")
    if len(score) == 0:
        break
    scores.append(int(score))

avg = sum(scores) / len(scores)
sd = 0
for i in range(len(scores)):
    sd += (scores[i] - avg) ** 2
sd = (sd / ((len(scores) - 1))) ** 0.5

print(f"Average score is {avg:.2f}")
print(f"Standard deviation is {sd:.2f}")

for i in range(len(scores)):
    print(f"Score #{i+1}: {scores[i]} grade: {calGrades(scores[i])}")
