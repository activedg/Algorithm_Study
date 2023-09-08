import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
# N+1일째 되는 날 퇴사하기, 남은 N일 동안 최대한 많은 상담
T, P = [], []
for _ in range(N):
    x, y = map(int, inp().split())
    T.append(x)
    P.append(y)
# i 번째 날 까지의 상담 최댓값
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    # 이전 까지의 최댓값
    dp[i] = max(dp[i], dp[i-1])
    # 당일 포함
    j = i + T[i-1] - 1
    if j < N + 1:
        # i 일차에 상담이 겹칠 순 없으니 i - 1일차 까지의 값과 비교
        dp[j] = max(dp[j], dp[i-1] + P[i-1])
print(dp[-1])