import sys
from collections import deque
# 방향성이 있는 연결형 그래프 문제
inp = lambda : map(int, sys.stdin.readline().split())
N, M = inp()
hacks = [[] for _ in range(N+1)]
res, res_num = 0, []
for _ in range(M):
    ## a가 b를 신뢰 -> b를 해킹 시 a도 해킹됨
    a, b = inp()
    ## b를 해킹 -> a도 해킹 -> a에 딸린 것도 해킹
    hacks[b].append(a)
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    cnt = 1
    queue = deque([i])
    while queue:
        t = queue.popleft()
        for h in hacks[t]:
            if not visited[h]:
                visited[h] = True
                queue.append(h)
                cnt += 1
    if cnt > res:
        res_num.clear()
        res_num.append(i)
        res = cnt
    elif cnt == res:
        res_num.append(i)
print(*res_num)