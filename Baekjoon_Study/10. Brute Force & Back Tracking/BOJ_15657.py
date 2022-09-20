import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
num = sorted(map(int, inp()))
def dfs(k, res=[], prev=0):
    if k == M:
        print(*res)
        return
    for n in num:
        if n >= prev:
            prev = n
            res.append(n)
            dfs(k+1, res, prev)
            res.pop()
dfs(0)