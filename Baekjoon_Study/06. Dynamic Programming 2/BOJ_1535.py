import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
L = list(map(int, inp().split()))
J = list(map(int, inp().split()))
## 100 50 20 13
## 20 30 40 50
dp = [0] * 100
for i in range(N):
    for j in range(99, L[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - L[i]] + J[i])
print(dp[-1])