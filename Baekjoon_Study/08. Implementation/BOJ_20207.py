import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
start, end = sys.maxsize, 0
schedule = [0] * 366
for _ in range(N):
    s, e = map(int, inp().split())
    start = min(s, start)
    end = max(e, end)
    for i in range(s, e + 1):
        schedule[i] += 1
w, h = 0, 0
res = 0
for i in range(start, end + 1):
    if not schedule[i]:
        res += w * h
        w, h = 0, 0
    else:
        w += 1
        h = max(h, schedule[i])
res += w * h
print(res)