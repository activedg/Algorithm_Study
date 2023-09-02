import sys
inp = lambda : sys.stdin.readline()
# 지폐의 금액 => T원의 지폐를 동전으로
T = int(inp())
# 동전의 가지 수
k = int(inp())
# 각 동전의 금액과 개수
coins = []
for _ in range(k):
    p, n = map(int, inp().split())
    coins.append((p, n))
# dp[i]는 i원에 대한 동전 교환 경우의 수
dp = [0] * (T + 1)
dp[0] = 1

# coins = [(5, 3), (10, 2), (1, 5)]
# dp[20] = dp[20 - 10 * 1] + dp[20 - 10 * 2]

for coin, cnt in coins:
    for money in range(T, 0, -1):
        for i in range(1, cnt + 1):
            if money < coin * i: break
            dp[money] += dp[money - coin * i]
print(dp[-1])