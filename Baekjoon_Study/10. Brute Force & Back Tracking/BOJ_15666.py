import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
num = sorted(set(map(int, inp())))
def dfs(k, arr=[], prev=0):
    if k == M:
        print(*arr)
        return
    for a in num:
        if a >= prev:
            arr.append(a)
            prev = a
            dfs(k+1, arr, prev)
            arr.pop()
dfs(0)