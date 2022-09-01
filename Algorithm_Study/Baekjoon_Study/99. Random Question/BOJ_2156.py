import sys
inp = sys.stdin.readline
n = int(inp())
data = [int(inp()) for _ in range(n)]
data = [0] + data
dp = [0] * (n+1)
dp[1] = data[1]
if n > 1:
    dp[2] = data[1] + data[2]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-2] + data[i], dp[i-3] + data[i-1] + data[i])
print(dp[-1])