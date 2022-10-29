import sys
inp = lambda : map(int, sys.stdin.readline().split())
C, N = inp()
# 적어도 C명 늘이기 위해 투자해야 할 돈의 최솟값
## 12 2
## 3 5
## 1 1
### 3 * 2 + 1 * 2
data = [list(inp()) for _ in range(N)]
M = C + max(list(map(lambda x:x[1], data)))
# i명 늘이는데 필요한 최솟값 배열
dp = [0] + [sys.maxsize] * M
for cost, num in data:
    for i in range(num, M+1):
        dp[i] = min(dp[i-num] + cost, dp[i])
print(min(dp[C:]))