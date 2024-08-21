def lastElement(n):
    return n[-1]

string = [i for i in input("Enter list of tuple: ").split()]
List = []
for num in string:
    List.append(tuple(int(i) for i in num.replace("", " ").split()))
print("Input list:", List)
print("Output list:", sorted(List, key=lastElement))
