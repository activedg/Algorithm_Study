import sys
from collections import deque
inp = lambda : sys.stdin.readline().split()
# 10 x 10 100개의 보드판
# 도착한 칸이 사다리면 위로 올라가기, 뱀이면 뱀 따라 내려가기
## 사다리 수 N, 뱀의 수 M
## 사다리 만나면 x -> y, 뱀 만나면 y -> x
N, M = map(int, inp())
ladder = dict()
snake = dict()
# 사다리 입력받기
for _ in range(N):
    x, y = map(int, inp())
    ladder[x] = y
# 뱀 입력받기
for _ in range(M):
    u, v = map(int, inp())
    snake[u] = v
q = deque([1])
visited = [False] * 101
res = [0] * 101
while q:
    cur = q.popleft()
    if cur >= 100:
        print(res[-1])
        break
    for x in range(1, 7):
        next_cur = cur + x
        if next_cur <= 100 and not visited[next_cur]:
            if next_cur in ladder.keys():
                next_cur = ladder[next_cur]
            elif next_cur in snake.keys():
                next_cur = snake[next_cur]

            if not visited[next_cur]:
                visited[next_cur] = True
                res[next_cur] = res[cur] + 1
                q.append(next_cur)