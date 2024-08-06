N, M, K = [int(i) for i in input().split()]
slow, answer = 0, 0
space = []

broken = [int(i) for i in input().split()]

for i in range(M-1):
    space.append(broken[i+1] - broken[i] - 1)

if K < M and M > 0:
    space.sort()
    answer += sum(space[0:M-K])
print(answer)
