import sys
inp = lambda : int(sys.stdin.readline())
n = inp()
stair = [0]
for _ in range(n):
    stair.append(inp())
dp = [0] * (n + 1)
dp[1] = stair[1]
if n >= 2:
    dp[2] = stair[1] + stair[2]
for i in range(3, n+1):
    # 두 계단 직전 + 현재 계단, 세 계단 + 직전 계단 + 현재 계단
    dp[i] = stair[i] + max(dp[i-2], dp[i-3] + stair[i-1])
print(dp[-1])