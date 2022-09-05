import sys
from collections import deque
## 최소 시간 문제(BFS) + 0초인 경우 존재 -> 우선순위 제공 및 따로 append
N, K = map(int, sys.stdin.readline().split())
size = 100000
place = [-1] * (size + 1)
place[N] = 0
q = deque([N])
while q:
    t = q.popleft()
    ## t * 2 가 더 높은 우선 순위를 가지게 하기 위해
    if t * 2 <= size and place[t * 2] == -1:
        place[t * 2] = place[t]
        q.appendleft(t * 2)
    for i in (t-1, t+1):
        if 0 <= i <= size and place[i] == -1:
            place[i] = place[t] + 1
            q.append(i)
print(place[K])
