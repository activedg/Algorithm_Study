import sys
inp = lambda : int(sys.stdin.readline())
# 병에서 약 하나 꺼내서 반으로 쪼개서 한 조각 먹고 다른 조각은 병에 넣는다
# 반 조각 꺼내면 -> 약 먹기, 아니면 반 쪼개서 먹고 다른 하나 넣기
# 한 조각 꺼낸 날에는 W, 반 조각 꺼낸 날에는 H 보내기
## W N번, H N번
dp = [[0] * 31 for _ in range(31)]
for j in range(31):
    dp[0][j] = 1
# 알약 반 개 i번, 한 개 j 번 => dp[i][j]
for i in range(1, 31):
    # 앞에서부터 순서대로 진행했을 때 H의 개수가 W의 개수보다 적으면 안됨
    for j in range(i, 31):
        # 알약 반 개를 i-1번, 알약 한 개를 j번 먹은 경우에서 반 개 먹는 경우 + 알약 반 개를 i 번, 알약 한 개를 j-1번에 알약 한 개 먹는 경우
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
while True:
    N = inp()
    if not N: break
    print(dp[N][N])