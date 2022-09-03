import sys
from collections import deque
# BFS 응용 문제
## 최단 시간 문제 -> BFS로 풀이 시작
inp = lambda : sys.stdin.readline().rstrip()
R, C = map(int, inp().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
## 지훈이의 위치에 대한 큐와 불의 위치에 대한 큐
q, fire_q = deque(), deque()
miro = []
for i in range(R):
    t = list(inp())
    miro.append(t)
    for j in range(C):
        if t[j] == 'J':
            q.append((i, j))
        elif t[j] == 'F':
            fire_q.append((i, j))
res = 0
while True:
    # 매 분마다 불, 지훈 이동
    res += 1
    temp = []
    ## 불 먼저 이동
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and miro[nx][ny] != '#' and miro[nx][ny] != 'F':
                temp.append((nx, ny))
                miro[nx][ny] = 'F'
    fire_q = deque(temp)
    temp = []
    while q:
        x, y = q.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(res)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and miro[nx][ny] == '.':
                temp.append((nx, ny))
                miro[nx][ny] = 'V'
    q = deque(temp)
    if not q: break
print('IMPOSSIBLE')