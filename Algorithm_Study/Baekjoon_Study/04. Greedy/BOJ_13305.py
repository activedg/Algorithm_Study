import sys
inp = sys.stdin.readline
n = int(inp())
path = list(map(int, inp().split()))
cost = list(map(int, inp().split()))
res, cost_min = path[0] * cost[0], cost[0]
for i in range(1, n-1):
    if cost[i] < cost_min:
        cost_min = cost[i]
        res += cost_min * path[i]
    else:
        res += cost_min * path[i]
print(res)