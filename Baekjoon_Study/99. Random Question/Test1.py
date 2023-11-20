from collections import deque


def solution(boards):
    # 상, 하, 좌, 우 4 방향중 하나 선택
    # 장애물이나 맨 끝에 부딪힐 때 까지 미끄러져 이동하는 것을 한 번으로
    # G 위치에 멈춰 서야함
    gx, gy = -1, -1
    q = deque()
    N, M = len(boards), len(boards[0])
    for i in range(N):
        for j in range(M):
            if boards[i][j] == 'R':
                q.append((i, j))
            elif boards[i][j] == 'G':
                gx, gy = i, j

    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)

    visited = [[0 for _ in range(M)] for _ in range(N)]

    while q:
        x, y = q.popleft()
        if x == gx and y == gy: break

        for i in range(4):
            tx, ty = x, y
            while True:
                nx, ny = tx + dx[i], ty + dy[i]
                if nx < 0 or nx >= N or ny < 0 or ny >= M:
                    visited[tx][ty] = visited[x][y] + 1
                    q.append((tx, ty))
                    break

                if boards[nx][ny] == 'D' and not visited[tx][ty]:
                    visited[tx][ty] = visited[x][y] + 1
                    q.append((tx, ty))
                    break

                if visited[nx][ny]: break

                tx, ty = nx, ny

    return visited[gx][gy]
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))