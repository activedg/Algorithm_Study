import sys
from collections import deque
inp = lambda : sys.stdin.readline().split()
# 길이가 N인 컨베이어 벨트
# 1번 칸은 올리는 위치, N번칸은 내리는 위치
# i번칸의 내구도는 Ai
# 로봇은 올리는 위치에만 올릴 수 있음, 내리는 위치에 오면 무조건 내림
# 로봇을 올리는 위치에 올리거나 이동하면 즉시 내구도 감소
# 로봇과 함께 한 칸 회전
## 가장 먼저 벨트에 올라간 로봇부터 이동, 이동할 수 없다면 가만히 있어야함
N, K = map(int, inp())
A = list(map(int, inp()))
robots = []
def rotate():
    global A, robots
    A = [A[-1]] + A[:2 * N - 1]
    # 로봇의 pos도 이동하기
    temp = []
    for i in range(len(robots)):
        robots[i] = (robots[i] + 1) % (2 * N)
        if robots[i] == N - 1: continue
        temp.append(robots[i])
    robots = temp
cur, cnt = 0, 0
while cnt < K:
    rotate()
    # 가장 먼저 올라간 로봇 부터 이동할 수 있다면 이동
    if robots:
        for _ in range(len(robots)):
            r = robots.pop(0)
            # 한 칸 이동
            nr = (r + 1) % (2 * N)
            # 로봇이 없는 칸이며 내구도 1 이상 이어야 함
            if nr not in robots and A[nr] >= 1:
                A[nr] -= 1
                if not A[nr]: cnt += 1
                if nr == N - 1: continue
                robots.append(nr)
            else:
                robots.append(r)


    if A[0]:
        A[0] -= 1
        if not A[0]: cnt += 1
        robots.append(0)
    cur += 1

print(cur)