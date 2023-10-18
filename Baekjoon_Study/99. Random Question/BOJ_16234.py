import sys
from collections import deque
# N x N 크기의 땅
# r행 c열에는 A[r][c]명 살고 있음
# 인접한 나라 사이에는 국경선 존재

# 인구 이동 하루 동안 진행, 더 이상 아래 방법에 의해 인구 이동이 없을 때 까지 지속됨
## L <= 국경선을 공유하는 두 나라의 인구 차이 <= R -> 국경선 연다
## 국경선 모두 열면 시작
## 인접한 칸만을 이용해 이동할 수 있음 -> 연합
## 연합을 이루고 있는 각 칸의 인구수 = (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
# 인구 이동 며칠 발생하는지
inp = lambda : sys.stdin.readline().split()
N, L, R = map(int, inp())
A = [list(map(int, inp())) for _ in range(N)]

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)

def bfs(i, j):
    path = [(i, j)]
    visited[i][j] = True
    q = deque(path)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                temp = abs(A[x][y] - A[nx][ny])
                if L <= temp <= R:
                    path.append((nx, ny))
                    visited[nx][ny] = True
                    q.append((nx, ny))

    return path

def move(arr):
    total, N = sum(A[x][y] for x, y in arr), len(arr)
    for x, y in arr:
        A[x][y] = total // N


res = 0
while True:
    visited = [[False for _ in range(N)] for _ in range(N)]
    unions = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                temp = bfs(i, j)
                if len(temp) > 1: unions.append(temp)

    if not unions: break
    for union in unions:
        move(union)
    res += 1
print(res)
