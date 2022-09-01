import sys
inp = sys.stdin.readline
N = int(inp())
count = {1: 0, 2: 1}
## Top Down
# 2로 나누는 것과 3으로 나누는 것 사이에 우선 순위 x
def dp(n):
    if n in count:
        return count[n]
    count[n] = 1 + min(dp(n//2) + n % 2, dp(n//3) + n % 3)
    return count[n]
print(dp(N))

## Bottom up
# count = [0] * (N + 1)
# for i in range(2, N+1):
#     count[i] = count[i-1] + 1
#     if not i % 3:
#         count[i] = min(count[i//3] + 1, count[i])
#     if not i % 2:
#         count[i] = min(count[i//2] + 1, count[i])
# print(count[N])