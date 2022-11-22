import sys
input = lambda : sys.stdin.readline()
def f(idx, time):
    if time > K:
        return -sys.maxsize
    if idx == N:
        return 0
    if dp[idx][time] != 0:
        return dp[idx][time]
    dp[idx][time] = max(f(idx + 1, time + li[idx][0]) + li[idx][1], f(idx + 1, time + li[idx][2]) + li[idx][3])
    return dp[idx][time]
N, K = map(int, input().split())
li = [[int(x) for x in input().split()] for _ in range(N)]
dp = [[0 for _ in range(100001)] for _ in range(N)]
print(f(0, 0))
# import sys
# from collections import defaultdict
# inp = lambda : map(int, sys.stdin.readline().split())
# # 서울에서 경산까지 구간이 N개
# # 인접한 도로 사이 자전거로 오느냐, 도보로 오느냐 모금액과 시간 차이
# N, K = inp()
# walk, bicycle = [], []
# for _ in range(N):
#     walk_time, walk_money, bicycle_time, bicycle_money = inp()
#     # (time, money)형식으로 append
#     walk.append((walk_time, walk_money))
#     bicycle.append((bicycle_time, bicycle_money))
# res = 0
# ## 백 트래킹으로 풀 경우 N이 커지는 경우 시간초과 발생
