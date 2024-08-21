List = eval(input("InputList: "))
answer = []
same = ""
for each in List:
    if each != same:
        answer.append(each)
    same = each
print(answer)
