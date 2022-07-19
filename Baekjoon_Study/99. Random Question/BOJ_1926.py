import sys
from collections import deque
inp = lambda : sys.stdin.readline().split()
n, m = map(int, inp())
draw = [list(map(int, inp())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(start_x, start_y):
    visited[start_x][start_y] = True
    res = 1
    q = deque([(start_x, start_y)])
    while q:
        temp = q.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if 0<=x<n and 0<=y<m and draw[x][y] and not visited[x][y]:
                visited[x][y] = True
                res += 1
                q.appendleft((x, y))
    return res
cnt, wide = 0, 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and draw[i][j]:
            cnt += 1
            wide = max(bfs(i, j), wide)
print(cnt)
print(wide)