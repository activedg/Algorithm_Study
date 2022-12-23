import sys
from collections import deque
inp = lambda : sys.stdin.readline()
N = int(inp())
road = list(map(int, inp().split()))
# 시작 index
s = int(inp()) - 1
visited = [False] * N
q = deque([s])
visited[s] = True
while q:
    t = q.popleft()
    for i in (t - road[t], t + road[t]):
        if i < 0 or i >= N: continue
        if not visited[i]:
            visited[i] = True
            q.append(i)
print(sum(1 for v in visited if v))
