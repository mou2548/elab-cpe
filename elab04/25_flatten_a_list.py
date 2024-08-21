answer = []
def flat(List):
    for each in List:
        if type(each) is not list:
            answer.append(each)
        else:
            flat(each)
    return answer

List = eval(input("Original list: "))
print(f"Flatten list: {flat(List)}")
