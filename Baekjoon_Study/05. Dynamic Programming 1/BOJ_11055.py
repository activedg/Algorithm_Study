import sys
inp = lambda : sys.stdin.readline()
# 증가하는 부분 수열 중 합이 가장 큰 것
N = int(inp())
A = list(map(int, inp().split()))
# 1 100 2 50 60 3 5 6 7 8
dp = [0 for _ in range(N)]
dp[0] = A[0]
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[j] + A[i], dp[i])
    dp[i] = max(dp[i], A[i])
print(max(dp))