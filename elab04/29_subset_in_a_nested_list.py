def checkSubset(list1, list2):
    if len(list1) > len(list2):
        m = list1
        n = list2
    else:
        n = list1
        m = list2
    for i in n:
        if i not in m:
            return False
    return True
