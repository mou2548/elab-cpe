Input = eval(input("Input: "))
List = [str(i) for i in Input]
countDict = {}
for i in List:
    if i in countDict:
        countDict[i] += 1
    else:
        countDict[i] = 1

maximum = max(countDict.values())
for i in range(maximum, 0, -1):
    for each in countDict.keys():
        if countDict[each] == i:
            print(f"{each}: {countDict[each]}")
