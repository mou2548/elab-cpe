h_shift = int(input("Enter horizontal shift size: "))
v_shift = int(input("Enter vertical shift size: "))

image = []
print("Enter image:")
while True:
    temp = input()
    if temp == '-1':
        break
    image.append(temp)

print("After shift:")
for i in range(v_shift):
    print('0' * len(image[0]))

for i in range(len(image) - v_shift):
    print('0' * h_shift, end="")
    print(image[i][:len(image[i])-h_shift])
