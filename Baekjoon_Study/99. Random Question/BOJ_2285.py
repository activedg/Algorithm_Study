import sys
inp = sys.stdin.readline
village = {}
for _ in range(int(inp())):
    a, b = map(int, inp().split())
    village[a] = b
min_dist = [sys.maxsize, 0]
keys = sorted(village.keys())
for k in keys:
    temp = sum(abs(i-k)*village[i] for i in keys if i != k)
    if temp < min_dist[0]:
        min_dist = [temp, k]
print(min_dist[1])