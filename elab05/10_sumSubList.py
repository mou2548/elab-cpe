def badInput(x, y):
    x_invalid = False
    y_invalid = False
    if x > len_list - 1 or x < -(len_list):
        x_invalid = True
    if y > len_list - 1 or y < -(len_list):
        y_invalid = True
    if x_invalid and y_invalid:
        return "x and y Bad Input"
    elif x_invalid:
        return "x Bad Input"
    elif y_invalid:
        return "y Bad Input"
    else:
        return None

List = [int(i) for i in input().split()]
len_list = len(List)
while True:
    x, y = input().split()
    x, y = int(x), int(y)

    if badInput(x, y):
        print(badInput(x, y))
        continue

    if x < 0:
        x += len_list
    if y < 0:
        y += len_list
    if x > y:
        break
    print(sum(List[x:y+1]))

    