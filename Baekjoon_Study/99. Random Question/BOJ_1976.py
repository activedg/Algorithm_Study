import sys
from collections import defaultdict, deque
inp = lambda : sys.stdin.readline()
# 도시의 수 N, 여행 계획에 속한 도시들 수 M
# (i, j) -> i번 도시와 j번 도시 연결 정보
## 그래프 탐색으로 풀었는데, 분리집합으로 풀면 더 빠르다
N = int(inp())
M = int(inp())
graph = defaultdict(list)
for i in range(N):
    temp = list(map(int, inp().split()))
    for j in range(N):
        if temp[j] == 1:
            graph[i+1].append(j+1)
travel = list(map(int, inp().split()))
res = True
for i in range(M-1):
    start, dest = travel[i], travel[i+1]
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    check = False
    while q:
        temp = q.popleft()
        if temp == dest:
            check = True
            break
        for pos in graph[temp]:
            if not visited[pos]:
                q.append(pos)
                visited[pos] = True
    if not check:
        res = False
        break
print("YES" if res else "NO")