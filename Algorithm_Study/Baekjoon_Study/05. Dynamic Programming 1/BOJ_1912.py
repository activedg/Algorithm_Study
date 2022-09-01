import sys
inp = sys.stdin.readline
n = int(inp())
data = list(map(int, inp().split()))
dp = [0] * n
dp[0] = data[0]
# dp (bottom up 방식) -> 점화식 기반 연산 -> 배열에 저장
for i in range(1, n):
    dp[i] = max(dp[i-1] + data[i], data[i])
print(max(dp))