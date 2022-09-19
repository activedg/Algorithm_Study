import sys
N, M = map(int, sys.stdin.readline().split())
def dfs(k, res = [], prev=0):
    if k == M:
        print(*res)
        return
    for i in range(1, N+1):
        if i >= prev:
            prev = i
            res.append(i)
            dfs(k+1, res, prev)
            res.pop()
dfs(0)