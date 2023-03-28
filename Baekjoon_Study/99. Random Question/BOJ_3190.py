import sys
from collections import deque
inp = lambda : sys.stdin.readline().rstrip()
# 사과 먹으면 뱀 길이 늘어남 -> 뱀 기어다니다 벽 또는 자기 자신의 몸과 부딪히면 끝
# NxN 보드, 몇몇 칸에는 사과
# 뱀 처음엔 오른쪽 향함
## 뱀은 몸 길이를 늘려 머리 다음칸에 위치
## 이동한 칸에 사과 있따면 사과 없어지고 꼬리 움직이지 X -> 머리만 이동한거
## 사과 없다면 몸 길이 줄여서 꼬리칸 비우기 -> 몸길이 변화 X
N = int(inp())
boards = [[0 for _ in range(N)] for _ in range(N)]
# 시계방향 순서 우->하->좌->상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_idx = 0
# 사과 정보
## 사과 있는 칸 1로 표기
K = int(inp())
for _ in range(K):
    x, y = map(int, inp().split())
    boards[x-1][y-1] = 1
# 방향 변환 횟수
L = int(inp())
move_idx = 0
moves = []
for _ in range(L):
    X, C = inp().split()
    moves.append((int(X), C))
res = 1
paths = deque([(0, 0), (0, 1)])
while True:
    # 벽에 닿은 겨우 break
    # x, y -> 현재 위치
    x, y = paths.pop()
    if x < 0 or x >= N or y < 0 or y >= N:
        break
    # 뱀의 몸이 있는 곳은 값이 2
    # print(x, y, boards[x][y])
    if boards[x][y] == 2:
        break

    # 사과 없는 칸 -> 꼬리 제거
    elif boards[x][y] == 0:
        r, c = paths.popleft()
        boards[r][c] = 0
    # 사과 있는 칸인 경우
    paths.append((x, y))
    boards[x][y] = 2
    if move_idx < L and res == moves[move_idx][0]:
        # idx 회전
        if moves[move_idx][1] == 'D':
            cur_idx += 1
        else:
            cur_idx -= 1
        cur_idx %= 4
        move_idx += 1
    res += 1
    paths.append((x + dx[cur_idx], y + dy[cur_idx]))
print(res)