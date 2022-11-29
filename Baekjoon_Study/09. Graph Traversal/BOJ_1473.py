import sys
from collections import deque
inp = lambda : map(int, sys.stdin.readline().split())
# N은 행의 개수, M은 열의 개수, K는 음식물 쓰레기 개수
N, M, K = inp()
# food_map 값이 0 : 방문, 1 : 음식물 있는 곳, -1 : 없는 곳
food_map = [[-1] * (M + 1) for _ in range(N+1)]
for _ in range(K):
    r, c = inp()
    food_map[r][c] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
res = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if food_map[i][j] == 1:
            temp = 0
            q = deque([(i, j)])
            while q:
                r, c = q.popleft()
                for k in range(4):
                    nx = dx[k] + r
                    ny = dy[k] + c
                    if 0 < nx <= N and 0 < ny <= M and food_map[nx][ny] == 1:
                        q.append((nx, ny))
                        temp += 1
                        food_map[nx][ny] = 0
            res = max(res,temp)
print(res)