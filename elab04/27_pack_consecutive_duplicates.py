List = eval(input("InputList: "))
temp = []
same = List[0]
group = []
for num in List:
    if num != same:
        group.append(temp)
        temp = []
    temp.append(num)
    same = num

group.append(temp)
print(group)
