string1 = input("Input string: ")
string2 = input("Input string: ")

for c in string1:
    if c in string2:
        string1 = string1.replace(c, "")
        string2 = string2.replace(c, "")

print(string1 + string2)
