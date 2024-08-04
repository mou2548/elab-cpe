def merge(a, b):
    A = a[:]
    B = b[:]
    res = []

    if type(A[0]) == int:
        while len(A) > 0 and len(B) > 0:
            print(res)
            print("A[0] =", A[0], "B[0] =", B[0])
            if A[0] == B[0]:
                print("A[0] == B[0]: pop = ", A[0], B[0])
                res.append(A.pop(0))
                res.append(B.pop(0))
            elif A[0] < B[0]:
                print("A[0] < B[0]: pop = ", A[0])
                res.append(A.pop(0))
            else:
                print("A[0] > B[0]: pop = ", B[0])
                res.append(B.pop(0))

    elif type(A[0]) == str:
        while len(A) > 0 and len(B) > 0:
            print(res)
            print("A[0][0] =", A[0][0], "B[0][0] =", B[0][0])
            if A[0][0] == B[0][0]:
                for i in range(min(len(A[0]), len(B[0]))):
                    print(f"A[0][{i}] =", A[0][i], f"B[0][{i}] =", B[0][i])
                    if A[0][i] < B[0][i]:
                        print(f"A[0][{i}] < B[0][{i}]: pop = ", A[0])
                        res.append(A.pop(0))
                        break
                    elif B[0][i] < A[0][i]:
                        print(f"B[0][{i}] < A[0][{i}]: pop = ", B[0])
                        res.append(B.pop(0))
                        break
                print(f"B[0] == A[0]: pop = ", A[0], B[0])
                res.append(A.pop(0))
                res.append(B.pop(0))
            elif A[0][0] < B[0][0]:
                print(f"A[0][0] < B[0][0]: pop = ", A[0])
                res.append(A.pop(0))
            else:
                print(f"B[0][0] < A[0][0]: pop = ", B[0])
                res.append(B.pop(0))

    if len(A) > 0:
        print(res)
        print("len(A) still > 0\nA =", A)
        res.extend(A)
    elif len(B) > 0:
        print(res)
        print("len(B) still > 0\nB =", B)
        res.extend(B)
    return res


def getInput():
    a = eval(input('Enter list a: '))
    b = eval(input('Enter list b: '))
    return a,b

### main begins here
a,b = getInput()
res = merge(a,b)
print(res)
