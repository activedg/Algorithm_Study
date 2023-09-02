import sys
inp = lambda : sys.stdin.readline()
# 정수 n과 m이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 법, 수는 m개 이하
mod = 1000000009
# 2차원 dp 사용
dp = [[0 for _ in range(1001)] for _ in range(1001)]
dp[1][1] = 1
dp[2][1], dp[2][2] = 1, 1
dp[3][1], dp[3][2], dp[3][3] = 1, 2, 1

for i in range(4, 1001):
    for j in range(1, i + 1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-2][j-1] + dp[i-3][j-1]) % mod

for _ in range(int(inp())):
    n, m = map(int, inp().split())
    print(sum(dp[n][:m+1]) % mod)

# def get_dp(a, b):
#     if dp[a][b] > 0: return dp[a][b]
#     if b == 1: return dp[a][1]
#
#     # 1, 2, 3 한 번 씩 빼가면서 진행
#     for k in range(1, 4):
#         if a > k:
#             dp[a][b] += get_dp(a - k, b - 1)
#     return dp[a][b]



