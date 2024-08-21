a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
List = [a, b, c]
ans = ['A', 'B', 'C']
while sum(List) != 1:
    low = List.index(min(List))
    for i in range(len(List)):
        if i == low:
            List[i] += 1
        else:
            List[i] -= 1

print(ans[List.index(max(List))])
