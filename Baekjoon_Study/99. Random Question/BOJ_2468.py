import sys
from collections import deque
inp = lambda : sys.stdin.readline()
N = int(inp())
rains = []
rain_min, rain_max = sys.maxsize, 0
for _ in range(N):
    rain = list(map(int, inp().split()))
    rain_min, rain_max = min(rain_min, min(rain)), max(rain_max, max(rain))
    rains.append(rain)
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(i, j, r, visit):
    q = deque([(i, j)])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if nx < 0 or nx >= N or ny < 0 or ny >= N: continue
            if rains[nx][ny] > r and not visit[nx][ny]:
                visit[nx][ny] = True
                q.append((nx, ny))
# 비 최솟값 부터 max - 1 까지 돌기
res = 1
for r in range(rain_min, rain_max):
    visited = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if rains[i][j] > r and not visited[i][j]:
                bfs(i, j, r, visited)
                cnt += 1
    res = max(res, cnt)
print(res)