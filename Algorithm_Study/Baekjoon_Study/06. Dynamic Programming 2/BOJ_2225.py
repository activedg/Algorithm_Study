import sys
inp = lambda : sys.stdin.readline().split()
N, K = map(int, inp())
mod = 1000000000
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][1] = 1
for j in range(2, K + 1):
    for i in range(N+1):
        # 3중 포문 안쓰고 (dp[i][j] = dp[0][j-1] + dp[1][j-1] + ... + dp[i-1][j-1] + dp[i][j-1]) dp[i-1][j] 사용
        dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[N][K] % mod)