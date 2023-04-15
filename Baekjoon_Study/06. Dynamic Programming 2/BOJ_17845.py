import sys
inp = lambda : sys.stdin.readline().split()
# 모든 과목의 중요도와 시간
# 공부시간 한계 초과 x -> 과목의 중요도 합이 최대가 되도록
N, K = map(int, inp())
value, time = [], []
for _ in range(K):
    v, t = map(int, inp())
    value.append(v)
    time.append(t)
# i-1번째의 공부를 포함하냐 마냐
# 2차원 dp or 1차원 dp 둘다 가능
# dp = [[0] * (N + 1) for _ in range(K+1)]
# for i in range(1, K+1):
#     for j in range(1, N+1):
#         # 시간 index가 현재 time보다 작으면 직전 값 그대로
#         if j < time[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i-1][j-time[i-1]] + value[i-1])
# print(dp[-1][-1])
dp = [0] * (N+1)
for i in range(K):
    t, v = time[i], value[i]
    for j in range(N, t-1, -1):
        dp[j] = max(dp[j], dp[j-t] + v)
print(dp[-1])