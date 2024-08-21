def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text

words = {}

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
strings = getMultilinesInput().lower().split()
k = int(input("Top K rank: "))
for string in strings:
    if string in words:
        words[string] += 1
    else:
        words[string] = 1

words = sorted(words.items(), key=lambda item:item[1], reverse=True)
answers = []
if len(words) > 0:
    temp = [words[0]]
    k -= 1

for word in words[1:]:
    if k < 0:
        break
    if word[1] == temp[-1][1]:
        temp.append(word)
    else:
        answers.append(temp)
        temp = [word]
        k -= 1

if k > 0:
    answers.append(temp)

for answer in answers:
    print(", ".join([f'{word}: {count}' for word, count in answer]))


        