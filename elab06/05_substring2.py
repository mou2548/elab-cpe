text = input("Text: ")
substring = input("Substring: ")
substring_len = len(substring)

answer = ''
i = 0
hasReal = False

while i < len(text):
    if len(text[i:i+substring_len]) < substring_len:
        break

    diff = sum(1 for a, b in zip(text[i:i+substring_len], substring) if a != b)
    if diff == 0:
        hasReal = True
        break
    i += 1

i = 0
while i < len(text):
    temp = ''
    if len(text[i:i+substring_len]) < substring_len:
        answer += text[i:]
        break
    
    diff = sum(1 for a, b in zip(text[i:i+substring_len], substring) if a != b)
    if hasReal and diff == 0:
        temp = f"[{substring}]"
    elif (not hasReal) and diff == 1:
        temp = '['
        for j in range(substring_len):
            if text[i+j] != substring[j]:
                temp += '?'
            else:
                temp += text[i+j]
        temp += ']'
    else:
        temp = text[i]

    answer += temp
    i += len(temp.lstrip('[').rstrip(']'))

print(answer)
