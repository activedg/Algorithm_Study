import sys, bisect
inp = lambda : sys.stdin.readline().rstrip()
for _ in range(int(inp())):
    n, m = map(int, inp().split())
    a = list(map(int, inp().split()))
    b = sorted(list(map(int, inp().split())))
    res = 0
    for t in a:
        idx = bisect.bisect_left(b, t)
        if idx == m:
            res += b[m-1]
        elif not idx:
            res += b[0]
        elif abs(t - b[idx-1]) <= abs(t - b[idx]):
            res += b[idx-1]
        else:
            res += b[idx]
    print(res)