def countStr(strList):
    count = 0
    for string in strList:
        if len(string) >= 2:
            if string[0] == string[-1]:
                count += 1
    return count

strList = input("Enter a set of strings: ").split()
print(countStr(strList))
