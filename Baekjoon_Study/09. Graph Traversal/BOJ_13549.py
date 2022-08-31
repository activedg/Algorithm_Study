import sys
from collections import deque
inp = lambda : map(int, sys.stdin.readline().split())
N, K = inp()
max_size = 100000
visit = [-1] * (max_size + 1)
visit[N] = 0
q = deque([N])
## t * 2 로 순간이동 하는 경우 코스트가 0인 것 고려
while q:
    t = q.popleft()
    if t == K: break
    for i in (t*2, t+1, t-1):
        if 0 <= i <= max_size and visit[i] == -1:
            if i == t*2:
                visit[i] = visit[t]
            else: visit[i] = visit[t] + 1
            q.append(i)
print(visit[K])