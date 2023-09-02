import sys
inp = lambda : sys.stdin.readline()
n, k = map(int, inp().split())
# 사용한 동전 구성이 같은데 순서만 다른 것 => 같은 경우
## 2 + 3 / 3 + 2 같은 경우
coins = [int(inp()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1
# 동전 for문 돌아가면서 dp 배열에 넣기
for coin in coins:
    for t in range(coin, k+1):
        dp[t] += dp[t - coin]
print(dp[-1])


## 시간 초과 풀이
# dp = [0] * (k+1)
# dp[0] = 1
# # 동전 개수 제한 없음
# for coin in coins:
#     for money in range(k, 0, -1):
#         i = 1
#         while money >= coin * i:
#             dp[money] += dp[money - coin * i]
#             i += 1
# print(dp[-1])