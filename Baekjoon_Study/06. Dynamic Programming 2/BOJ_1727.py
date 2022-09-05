import sys
inp = lambda: map(int, sys.stdin.readline().split())
n, m = inp()
men = sorted(inp())
women = sorted(inp())
# men, women -> 남자 i번 여자 j번 까지 커플의 성격차 합 -> dp로 bottom up 하면서 올리기 + 남자나 여자가 더 많은 경우 성격차 더 적은 것 선택
## 최적의 해 조건 // 정렬 되어 있는 상황 이므로 리스트에 X자로 매칭되는 경우 없음
dp = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        ## 남자가 더 많은 경우 -> i번째 남자가 솔로 vs 커플(선택 됨)
        if i > j:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1] + abs(women[j-1] - men[i-1]))
        elif i < j:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j-1] + abs(women[j-1] - men[i-1]))
        else:
            dp[i][j] = dp[i - 1][j - 1] + abs(women[j - 1] - men[i - 1])
print(dp[-1][-1])
