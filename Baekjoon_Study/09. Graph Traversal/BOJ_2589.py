import sys
from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
inp = lambda : sys.stdin.readline()
n, m = map(int, inp().split())
res = 0
## bfs를 브루트 포스 하면서 끝나는 지점 마다 움직인 횟수 갱신
board = []
for _ in range(n):
    board.append(list(inp().rstrip()))
def bfs(start_x, start_y):
    temp = 0
    q = deque([(start_x, start_y)])
    visited = [[0] * m for _ in range(n)]
    visited[start_x][start_y] = 1
    ## 1 설정 안해둘 경우 시작점 재방문 될 가능성 있음
    while q:
        x, y = q.popleft()
        checker = False
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and board[new_x][new_y] == 'L' and not visited[new_x][new_y]:
                visited[new_x][new_y] = visited[x][y] + 1
                q.append((new_x, new_y))
                checker = True
        if not checker:
            temp = max(temp, visited[x][y] - 1)
    return temp
res = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 'L':
            res = max(res, bfs(i, j))
print(res)