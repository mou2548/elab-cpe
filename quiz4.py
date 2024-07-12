def getList():
    layer = []
    temp = (input("ผลการสำรวจ: ").split())
    for i in range(len(temp)):
        layer.append(int(temp[i])) ## make list
    return layer

def findTallestIndex():
    for i in range(len(layer)):
        if layer[i] == tallest:
            tallest_index = i
    return tallest_index

def printMap():
    for i in range(tallest): ## print map
        for j in range(len(layer)):
            con = layer[j] - tallest + i
            if con >= 0:
                if con < 4:
                    print("o", end="")
                elif con >= 4 and con < 8:
                    print("=", end="")
                else:
                    print("x", end="")
            else:
                print(" ", end="")
        print()

def printFlag():
    flag = ["+-------+", "| CPE38 |", "+-------+", "|", "|", "|"]
    for i in range(6):
        print(" " * tallest_index, end="")
        print(flag[i][0:len(layer)-tallest_index])

layer = getList()
tallest = max(layer)
tallest_index = findTallestIndex()

print("แผนที่:")
printMap()
print("อาจารย์โตโต้เดินทางไปปักธงที่จุดยอดสูงสุด:")
printFlag()
printMap()
