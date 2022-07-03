import sys
from collections import deque
# BFS 풀이법
N, K = map(int, sys.stdin.readline().split())
q = deque([N])
MAX = 100000
visit = [-1] * (MAX + 1)
visit[N] = 0
while q:
    t = q.popleft()
    if t == K:
        print(visit[t])
        break
    for i in (t-1, t+1, t * 2):
        if 0 <= i <= MAX and visit[i] == -1:
            q.append(i)
            visit[i] = visit[t] + 1

## Another Solution
# 재귀 -> find 함수 이용
def find(n, k):
    if n >= k:
        return n-k
    elif k == 1:
        return 1
    elif k % 2:
        return min(find(n, k-1), find(n, k+1) + 1)
    else:
        return min(k-n, find(n, k//2) + 1)
