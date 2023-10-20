import sys
inp = lambda : sys.stdin.readline().split()
# 리조트 하루 이용권 만원
# 3일 이용권 + 쿠폰 1장 : 2만 5천원, 5일 이용권 + 쿠폰 2 장 3만 7천원
# 쿠폰 3장 == 하루 이용권 한장
## 연속으로 3일, 5일만 가능하지만 다 이용할 필요는 X
# 리조트에 갈 수 없는 날 M일 -> 그 외 모든 날 리조트에서
N, M = map(int, inp())
avail = [True for _ in range(N+1)]
for a in map(int, inp()):
    avail[a] = False
# 쿠폰 갯수에 대한 것을 dp로 어떻게 나타낼 지?
K = max((N // 5) * 2, N // 3)
dp = [[sys.maxsize for _ in range(K+1)] for _ in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(min(K, i) + 1):
        # 1일 권 사용
        # 스케줄 있는 날이면 스킵
        if avail[i]:
            dp[i][j] = min(dp[i-1][j] + 10000, dp[i][j])
        else:
            dp[i][j] = min(dp[i-1][j], dp[i][j])

        # 3일 권 사용
        if i >= 3 and j >= 1:
            dp[i][j] = min(dp[i-3][j-1] + 25000, dp[i][j])

        # 5일 권 사용
        if i >= 5 and j >= 2:
            dp[i][j] = min(dp[i-5][j-2] + 37000, dp[i][j])

        # 쿠폰 사용
        if avail[i] and j >= 3:
            dp[i][j-3] = min(dp[i - 1][j], dp[i][j-3])
print(min(dp[-1]))
