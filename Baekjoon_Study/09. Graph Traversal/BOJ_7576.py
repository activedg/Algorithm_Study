import sys
from collections import deque
inp = lambda : map(int, sys.stdin.readline().split())
M, N = inp()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
tomato = []
q = deque([])
res = -1
for i in range(N):
    tomato.append(list(inp()))
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j))
# 가능한 인접한 노드 모드 방문 -> BFS로 풀기
while q:
    res += 1
    for _ in range(len(q)):
        x, y = q.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M and tomato[new_x][new_y] == 0:
                q.append((new_x, new_y))
                tomato[new_x][new_y] = 1
for t in tomato:
    if 0 in t:
        res = -1
        break
print(res)