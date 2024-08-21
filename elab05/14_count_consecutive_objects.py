def countConsec(List):
    if len(List) == 0:
        return 'Nothing to do.'
    combo = [[List[0], 1]]
    for each in List[1:]:
        if each == combo[-1][0]:
            combo[-1][1] += 1
        else:
            combo.append([each, 1])
    return [(value, count) for value, count in combo]

List = eval(input("Enter a list of objects: "))
if len(List) == 0:
    print(countConsec(List))
else:
    List = sorted(countConsec(List), key= lambda x: x[1], reverse=True)
    print(List[0][0])
    print(List[0][1])