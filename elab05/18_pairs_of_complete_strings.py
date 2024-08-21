set1 = eval(input("String set1: "))
set2 = eval(input("String set2: "))

answers = []

for each1 in set1:
    for each2 in set2:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        string = each1 + each2
        for c in string.lower():
            alphabets = alphabets.replace(c, "")
        if not alphabets:
            answers.append(string)

print("Output:", len(answers))
print("The total complete pairs that are forming are:")
for answer in answers:
    print("", answer)
