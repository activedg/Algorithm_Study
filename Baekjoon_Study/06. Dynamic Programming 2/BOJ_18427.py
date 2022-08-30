import sys
inp = lambda : map(int, sys.stdin.readline().split())
N, M, H = inp()
# 경우의 수 적어 가면서 점화식 세우기
## 1 0 1 1 0 1
## 1 0 1 2 0 3
## 1 1 2 4 3 6
## dp[1][5] -> 2번째 학생 까지 총합 무게 5/ 1번째 학생이 무게 5를 다한 경우 + 2번째 학생 까지 해서 무게 5를 하게된 경우
dp = [[1] + [0] * H for _ in range(N)]
for i in [0] + list(inp()):
    dp[0][i] = 1
for i in range(1, N):
    dp[i] = dp[i-1].copy()
    block = list(inp())
    for b in block:
        for j in range(b, H+1):
            dp[i][j] += dp[i-1][j-b]
print(dp[-1][-1] % 10007)