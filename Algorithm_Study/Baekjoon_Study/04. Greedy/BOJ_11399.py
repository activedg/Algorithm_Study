import sys
inp = sys.stdin.readline
N = int(inp())
time = sorted(list(map(int, inp().split())))
res = time[0]
for i in range(1, N):
    time[i] += time[i-1]
    res += time[i]
print(res)