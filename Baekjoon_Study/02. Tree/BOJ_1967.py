import sys
from collections import deque
inp = sys.stdin.readline
n = int(inp())
edges = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = map(int, inp().split())
    edges[a].append([b, w])
    edges[b].append([a, w])
def bfs(v):
    visit = [-1] * (n+1)
    q = deque([v])
    max_path = [0, 0]
    visit[v] = 0
    while q:
        t = q.popleft()
        for i, w in edges[t]:
            if visit[i] == -1:
                visit[i] = visit[t] + w
                q.append(i)
                if max_path[0] < visit[i]:
                    max_path = [visit[i], i]
    return max_path
start = bfs(1)[1]
print(bfs(start)[0])