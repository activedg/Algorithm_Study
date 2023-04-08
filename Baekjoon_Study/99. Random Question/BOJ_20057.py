import sys
inp = lambda : sys.stdin.readline()
# x 에서 y로 이동하면 y의 모든 모래가 비율과 a 적혀 있는 칸으로 이동
# a는 남은 양
# 계산에선 소수점 아래는 버리기
# 왼쪽으로 이동할 때 기준
## 격자의 밖으로 나간 모래의 양
# 좌 하 우 상 순으로 이동
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
N = int(inp())
sands = [list(map(int, inp().split())) for _ in range(N)]
cur_move, move_cnt = 1, 0
# 좌 하 우 상 배열 idx
idx = 0
res = 0
def tornado_turn(arr):
    result = [[0 for _ in range(5)] for _ in range(5)]
    for i in range(5):
        for j in range(5):
            result[5-j-1][i] = arr[i][j]
    return result
tornado_0 = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
tornado_1 = tornado_turn(tornado_0)
tornado_2 = tornado_turn(tornado_1)
tornado_3 = tornado_turn(tornado_2)
tornados = [tornado_0, tornado_1, tornado_2, tornado_3]

alphas = [(0, -1), (1, 0), (0, 1), (-1, 0)]
res = 0
# 현재 토네이도 방향
idx = 0
# 현재 토네이도 길이
tornado_length = 1
cur_move = 0
x, y = N // 2, N // 2
temp_cnt = 0
while not (x == 0 and y == 0):
    x, y = x + dx[idx], y + dy[idx]
    cur_move += 1
    cur_tornado = tornados[idx]
    temp = sands[x][y]
    sands[x][y] = 0
    left_sand = temp
    for r in range(5):
        for c in range(5):
            now_sand = int(temp * cur_tornado[r][c])
            left_sand -= now_sand
            if 0 <= x + r - 2 < N and 0 <= y + c - 2 < N:  # data 배열 안에 가능하다면 data 갱신
                sands[x + r - 2][y + c - 2] += now_sand
            else:  # 불가능 하다면 밖으로 나간 모래
                res += now_sand
    ## alpha 위치
    if 0 <= x + alphas[idx][0] < N and 0 <= y + alphas[idx][1] < N:
        sands[x + alphas[idx][0]][y + alphas[idx][1]] += left_sand
    else:
        res += left_sand

    # 방향 갱신
    if cur_move == tornado_length:
        cur_move = 0
        temp_cnt += 1
        idx = (idx + 1) % 4
        if temp_cnt == 2:
            tornado_length += 1
            temp_cnt = 0
print(res)