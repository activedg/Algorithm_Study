import sys
from collections import deque
inp = lambda : sys.stdin.readline()
# NxN 크기에 물고기 M마리와 아기 상어 1마리
# 한 칸에는 물고기 최대 1마리
# 가장 처음 크 기 2, 아기 상어 1초에 상하좌우 이동
dx = (0, 0, 1, -1)
dy = (-1, 1, 0, 0)
# 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없음
# 자신의 크기보다 작은 물고기만 먹을 수 있음
# 크기가 같은 물고기는 먹을수 없음, 지나가기는 가능

## 더 이상 먹을 수 있는 물고기가 없다면 끝
## 먹을 수 있는 물고기 1마리 이상 -> 거리가 가장 가까움
## 가장 위에 있는, 가장 왼쪽에 있는 물고기 먹기

## 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기 1 증가

N = int(inp())
boards = [[0 for _ in range(N)] for _ in range(N)]
cur_x, cur_y = 0, 0
for i in range(N):
    temp = list(map(int, inp().split()))
    for j in range(N):
        boards[i][j] = temp[j]
        if temp[j] == 9:
            # 위치 x, y
            cur_x, cur_y = i, j
            boards[i][j] = 0
# 크기, 경험치
size, exp = 2, 0

def find_path(i, j):
    q = deque([(i, j)])
    visited = [[0] * N for _ in range(N)]
    res = []
    visited[i][j] = 1
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if boards[nx][ny] > size or visited[nx][ny]: continue

                if 0 < boards[nx][ny] < size:
                    res.append([visited[x][y], nx, ny])
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    if not res: return []
    return sorted(res)[0]

res = 0
while True:
    # 길 찾기
    temp = find_path(cur_x, cur_y)

    if not temp: break

    cur_x, cur_y = temp[1], temp[2]
    boards[cur_x][cur_y] = 0
    exp += 1
    if size == exp:
        size, exp = size + 1, 0

    res += temp[0]
print(res)