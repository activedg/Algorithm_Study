import sys
inp = lambda : sys.stdin.readline().split()
R, C, T = map(int, inp())
# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# A, 공기 청정기 입력받기
A = [[0 for _ in range(C)] for _ in range(R)]
## https://recordofwonseok.tistory.com/360
cleaner = []
for i in range(R):
    temp = list(map(int, inp()))
    for j in range(C):
        if temp[j] == -1:
            cleaner.append(i)
        A[i][j] = temp[j]
# 미세먼지 확산, 미세먼지 있는 모든 칸에서 동시에
# 인접한 방향에 공기청정기, 먼지 있으면 확산 안됨
# 확산되는 야은 A[i][j]/ 5, 남은 미세먼지 양은 확산되고 남은거
# 미세먼지 확산 먼저 일어나고 공기청정기 작동
def spread():
    change = [[0 for _ in range(C)] for _ in range(R)]
    for x in range(R):
        for y in range(C):
            # 미세먼지 있는 경우
            if A[x][y] > 0:
                temp = 0
                for k in range(4):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C and A[nx][ny] != -1:
                        change[nx][ny] += A[x][y] // 5
                        temp += A[x][y] // 5
                A[x][y] -= temp
    for i in range(R):
        for j in range(C):
            A[i][j] += change[i][j]


def rotation():
    def top_rotate():  # 위쪽 회전
        d = 1  # 오른쪽 방향으로 시작
        before = 0
        x, y = cleaner[0], 1  # 공기청정기 머리부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:  # 현재 좌표가 꼭짓점인 경우
                d = (d - 1) % 4
                continue
            if x == cleaner[0] and y == 0:  # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            A[x][y], before = before, A[x][y]
            x, y = ax, ay

    def bottom_rotate():  # 아래 회전
        d = 1  # 오른쪽 방향으로 시작
        before = 0
        x, y = cleaner[1], 1  # 공기청정기 아래부분의 바로 오른쪽 칸부터 시작
        while True:
            ax = x + dx[d]
            ay = y + dy[d]
            if ax == R or ay == C or ax == -1 or ay == -1:  # 현재 좌표가 꼭짓점인 경우
                d = (d + 1) % 4
                continue
            if x == cleaner[1] and y == 0:  # 한 바퀴 회전 완료해서 공기청정기 좌표로 다시 돌아온 경우
                break
            A[x][y], before = before, A[x][y]
            x, y = ax, ay

    top_rotate()
    bottom_rotate()
for _ in range(T):
    spread()
    rotation()

res = 2
for i in range(R):
    res += sum(A[i])
print(res)
# while cur < T:
#     x, y, t = q.popleft()
#
#     if cur != t:
#         # 공기 정화 시작
#         cur = t
#         cur_x, cur_y = cleaner[0][0] - 1, cleaner[0][1]
#         top_idx = 0
#         # 공기청정기 바로 위 정화
#         A[cur_x][cur_y] = 0
#         cur_x -= 1
#         while cur_x != cleaner[0][0] or cur_y != cleaner[0][1]:
#             new_x, new_y = cur_x + top_x[top_idx], cur_y + top_y[top_idx]
#             if new_x < 0 or new_y >= C or new_x > cleaner[0][0]:
#                 top_idx += 1
#             else:
#                 if new_x == cleaner[0][0] and new_y == cleaner[0][1]:
#                     A[cur_x][cur_y] = 0
#                 else:
#                     A[cur_x][cur_y] = A[new_x][new_y]
#                 cur_x, cur_y = new_x, new_y
#
#         cur_x, cur_y = cleaner[1][0] + 1, cleaner[0][1]
#         bottom_idx = 0
#         A[cur_x][cur_y] = 0
#         cur_x += 1
#         while cur_x != cleaner[1][0] or cur_y != cleaner[1][1]:
#             new_x, new_y = cur_x + bottom_x[bottom_idx], cur_y + bottom_y[bottom_idx]
#             if new_x >= R or new_y >= C or new_x < cleaner[1][0]:
#                 bottom_idx += 1
#             else:
#                 if new_x == cleaner[1][0] and new_y == cleaner[1][1]:
#                     A[cur_x][cur_y] = 0
#                 else:
#                     A[cur_x][cur_y] = A[new_x][new_y]
#                 cur_x, cur_y = new_x, new_y
#
#         if cur == T: break
#         B = copy.deepcopy(A)
#
#     temp = []
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if nx < 0 or nx >= R or ny < 0 or ny >= C: continue
#         # 미세먼지 이동 가능 구간
#         if B[nx][ny] != -1:
#             temp.append((nx, ny, B[x][y] // 5))
#
#     for i, j, k in temp:
#         A[i][j] += k
#         A[x][y] -= k
#         q.append((i, j, t + 1))
#     q.append((x, y, t + 1))
# res = 0
# for a in A:
#     res += sum(i for i in a if i != -1)
#     print(*a)
# print(res)