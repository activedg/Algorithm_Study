import sys
# from itertools import permutations
# N, M = map(int, inp())
# num = [i for i in range(1, N+1)]
# perm = permutations(num, M)
# for p in perm:
#     print(*p)
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
using = [False] * (N+1)
num = [0] * M
def permutation(k):
    ## dfs에서 depth랑 비슷하게 생각
    if k == M:
        print(*num)
        return
    for i in range(1, N+1):
        if not using[i]:
            using[i] = True
            num[k] = i
            permutation(k+1)
            using[i] = False
permutation(0)