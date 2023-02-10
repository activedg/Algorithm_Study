import sys
inp = lambda : sys.stdin.readline()
# 집 빨강, 초록, 파랑 중 하나로 색 칠하기
## 1번 집의 색은 2번, N번과 같지 X
## N번 집의 색은 N-1, 1번 집의 색과 같지 X
## i번 집의 색은 i-1, i+1번 집의 색과 같지 X
N = int(inp())
# 2차원 dp
cost = [list(map(int, inp().split())) for _ in range(N)]
def rgb(start):
    dp = [[float("inf") for _ in range(3)] for _ in range(N)]
    for j in range(3):
        if j == start: continue
        dp[1][j] = cost[0][start] + cost[1][j]
    for i in range(2, N):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[i][2]
    return min(dp[-1][start-1], dp[-1][start-2])
res = float("inf")
for i in range(3):
    res = min(res, rgb(i))
print(res)