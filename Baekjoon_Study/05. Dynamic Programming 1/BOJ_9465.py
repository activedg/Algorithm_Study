import sys
inp = lambda: sys.stdin.readline()
for _ in range(int(inp())):
    n = int(inp())
    up_sticker = list(map(int, inp().split()))
    down_sticker = list(map(int, inp().split()))
    max_up = 0
    max_down = 0
    for i in range(n):
        max_up, max_down = max(max_down + up_sticker[i], max_up), max(max_up + down_sticker[i], max_down)
    print(max(max_up, max_down))

# def sticker_dp(s: list, n: int):
#     dp = [[0] * n for _ in range(2)]
#     dp[0][0], dp[1][0] = s[0][0], s[1][0]
#     if n > 1:
#         dp[0][1] = max(dp[0][0], dp[1][0] + s[0][1])
#         dp[1][1] = max(dp[1][0], dp[0][0] + s[1][1])
#     for j in range(2, n):
#         for i in range(2):
#             t = 1 if not i else 0
#             dp[i][j] = max(dp[i][j-1], dp[t][j-1] + s[i][j], dp[t][j-2] + s[i][j])
#     return max(dp[0][n-1], dp[1][n-1])