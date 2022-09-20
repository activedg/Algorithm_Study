import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
num = sorted(map(int, inp()))
using = [False] * N
def dfs(k, res=[]):
    if k == M:
        print(*res)
        return
    for i in range(N):
        if not using[i]:
            using[i] = True
            res.append(num[i])
            dfs(k+1, res)
            res.pop()
            using[i] = False
dfs(0)