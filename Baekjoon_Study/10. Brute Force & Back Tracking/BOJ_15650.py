import sys
N, M = map(int, sys.stdin.readline().split())
## 중복 X, 무조건 오름차순 수열
num = [0] * M
using = [False] * (N+1)
def permutation(k):
    if k == M:
        print(*num)
        return
    for i in range(1, N+1):
        if not k or num[k-1] < i:
            num[k] = i
            using[i] = True
            permutation(k+1)
            using[i] = False
permutation(0)