import sys
from collections import defaultdict, deque
inp = lambda : sys.stdin.readline().split()
# 6단계 이하로 연결되어 있으면 작은 세상
N, K = map(int, inp())
graph = defaultdict(list)
for _ in range(K):
    a, b = map(int, inp())
    graph[a].append(b)
    graph[b].append(a)
distances = [[sys.maxsize] * (N+1) for _ in range(N+1)]
check = False
for i in range(1, N+1):
    distances[i][i] = 0
for i in range(1, N+1):
    q = deque([i])
    visited = [False] * (N+1)
    visited[i] = True
    while q:
        t = q.popleft()
        for j in graph[t]:
            if not visited[j]:
                visited[j] = True
                q.append(j)
                distances[i][j] = min(distances[i][j], distances[i][t] + 1)
    if max(distances[i][1:]) > 6:
        check = True
print('Big World!') if check else print('Small World!')