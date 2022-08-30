import sys
from collections import deque
# 가장 빠른 시간 출력, 경우의 수와 혼합
inp = lambda : map(int, sys.stdin.readline().split())
N, K = inp()
visit = [-1] * 100001
visit[N] = 0
q = deque([N])
res = 0
while q:
    t = q.popleft()
    ## 반복문 종료 조건 기존과 다름
    if t == K:
        res += 1
    else:
        for i in (t-1, t+1, t*2):
            ## visit[i] 값이 -1말고도 다른 것도 따지기
            if 0<=i<=100000 and (visit[i] == -1 or visit[i] == visit[t] + 1):
                visit[i] = visit[t] + 1
                q.append(i)
print(visit[K])
print(res)
