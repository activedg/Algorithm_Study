import sys
inp = lambda : sys.stdin.readline().split()
# 각 단원별 예상 공부 시간 + 단원 문제 배점
N, T = map(int, inp())
study = [list(map(int, inp())) for _ in range(N)]
# 0-1 knapsack -> 시간 할애 총량이 T
dp = [0] * (T+1)
for time, value in study:
    for i in range(T, time-1, -1):
        dp[i] = max(dp[i], dp[i-time] + value)
print(dp[-1])
# dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
# for i in range(1, N+1):
#     time, value = study[i-1][0], study[i-1][1]
#     for j in range(1, T+1):
#         if j < study[i-1][0]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-time] + value)
# print(dp[-1][-1])