import sys
inp = lambda : sys.stdin.readline().rstrip()
X = list(inp())
Y = list(inp())
# dp[i][j] -> Xi 와 Yj의 최장 공통 부분 수열
dp = [["" for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
for i in range(1, len(X) + 1):
    for j in range(1, len(Y) + 1):
        if X[i-1] == Y[j-1]:
            dp[i][j] = dp[i-1][j-1] + X[i-1]
        else:
            if len(dp[i-1][j]) < len(dp[i][j-1]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
print(len(dp[-1][-1]))
print(dp[-1][-1])