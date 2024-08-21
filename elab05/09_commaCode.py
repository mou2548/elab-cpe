def commaCode(myList):
    if not myList:
        return ''
    if len(myList) == 1:
        return myList[0]
    return ", ".join(myList[:-1]) + ', and ' + myList[-1]


myList = input("Input: ").split()
print(commaCode(myList))
