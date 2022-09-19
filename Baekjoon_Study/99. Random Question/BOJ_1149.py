import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
house = [list(map(int, inp().split())) for _ in range(N)]
# 2차원 배열 사용
dp = [[0] * 3 for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + house[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + house[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + house[i-1][2]
print(min(dp[-1]))