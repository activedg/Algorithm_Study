import sys
inp = lambda : sys.stdin.readline()
for _ in range(int(inp())):
    N = int(inp())
    coins = list(map(int, inp().split()))
    M = int(inp())
    dp = [0] * (M+1)
    dp[0] = 1
    for c in coins:
        for i in range(1, M+1):
            if i >= c:
                dp[i] += dp[i-c]
    print(dp[M])