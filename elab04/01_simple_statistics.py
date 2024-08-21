List = []
while True:
    num = input("Enter a number (or [Enter] to stop): ")
    if len(num) == 0:
        break
    List.append(float(num))
    
if len(List) == 0:
    print("Nothing to do.")
else:
    print(f"Maximum value is {max(List):.2f}")
    print(f"Minimum value is {min(List):.2f}")
    print(f"Average value is {sum(List) / len(List):.2f}")
