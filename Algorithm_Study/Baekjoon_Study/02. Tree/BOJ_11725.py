import sys
from collections import deque
N = int(sys.stdin.readline())
graph = {}
parents, visited = [0] * (N+1), [False] * (N+1)
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    if a not in graph:
        graph[a] = [b]
    elif b not in graph[a]:
        graph[a].append(b)

    if b not in graph:
        graph[b] = [a]
    elif a not in graph[b]:
        graph[b].append(a)
stack = deque([1])
while stack:
    t = stack.popleft()
    visited[t] = True
    for i in graph[t]:
        if not visited[i]:
            stack.append(i)
            parents[i] = t
print('\n'.join(map(str, parents[2:])))