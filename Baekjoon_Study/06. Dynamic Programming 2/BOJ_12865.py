import sys
inp = lambda : sys.stdin.readline().split()
# https://velog.io/@jxlhe46/알고리즘-배낭-문제-Knapsack-Problem
N, K = map(int, inp())
items = [list(map(int, inp())) for _ in range(N)]
# 물건을 1~i까지만 고려하고 (임시) 배낭 용량이 w일 때 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
# 무게, 가치 순
for i in range(1, N+1):
    for j in range(1, K+1):
        w = items[i-1][0]
        # 물건 i의 무게가 임시 용량 초과시
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], items[i-1][1] + dp[i-1][j-w])
print(dp[N][K])