import sys
from itertools import combinations
inp = lambda : map(int, sys.stdin.readline().split())
# dp로 도전해보기
## N : 짜장면 수, M : 웍 수
N, M = inp()
works = list(inp())
dp = [sys.maxsize] * (N+1)
# 웍 한 개 사용도 가능, 두 개 사용도 가능
dp[0] = 0
for w in works:
    dp[w] = 1
work_set = set(works)
# 가능한 조합 set에다 추가하기
two_work = list(combinations(works, 2))
for w1, w2 in two_work:
    work_set.add(w1+w2)
# set을 정렬하고자 할 때는 list로 변환하는게 좋음
work_set = sorted(list(work_set))
for i in range(1, N+1):
    for w in work_set:
        if i - w >=0: dp[i] = min(dp[i-w] + 1, dp[i])
        else: break

if dp[N] < sys.maxsize: print(dp[N])
else: print(-1)
