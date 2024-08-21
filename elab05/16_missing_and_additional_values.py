list1 = eval(input("Input list1: "))
list2 = eval(input("Input list2: "))

list1_additional = []
list2_additional = []

for each in list1:
    if each not in list2:
        list1_additional.append(each)

for each in list2:
    if each not in list1:
        list2_additional.append(each)

print("Missing values in list1 =", list2_additional)
print("Additional values in list1 =", list1_additional)
print("Missing values in list2 =", list1_additional)
print("Additional values in list2 =", list2_additional)