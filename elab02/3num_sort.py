a = int(input())
b = int(input())
c = int(input())

if a < b and b < c:
    print(a, b, c)
elif a < b and c < b and a < c:
    print(a, c, b)
elif b < a and a < c and b < c:
    print(b, a, c)
elif b < c and c < a and b < a:
    print(b, c ,a)
elif c < a and a < b and c < b:
    print(c, a, b)
elif c < b and b < a and c < a:
    print(c, b, a)
