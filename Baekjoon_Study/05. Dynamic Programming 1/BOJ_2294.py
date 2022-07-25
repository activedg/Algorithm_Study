import sys
inp = lambda : sys.stdin.readline()
n, k = map(int, inp().split())
coin = sorted([int(inp()) for _ in range(n)])
dp = [10001] * (k+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k+1):
        dp[j] = min(dp[j], dp[j-coin[i]]+1)
print(dp[k]) if dp[k] != 10001 else print(-1)

# coin = sorted([int(inp()) for _ in range(n)], reverse=True)
# dp = [10001] * (k+1)
# for i in range(1, k+1):
#     for c in coin:
#         if i == c:
#             dp[i] = 1
#         elif i - c > 0:
#             if dp[i-c] != -1:
#                 dp[i] = min(dp[i], dp[i-c] + 1)
#             else: continue
#         else: continue
#     if dp[i] == 10001:
#         dp[i] = -1
# print(dp[k])