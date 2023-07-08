import sys
inp = lambda : sys.stdin.readline()
# 남은 N일 동안 최대한 많은 상담 하려함
# 상담을 완료하는데 걸리는 기간 Ti, 상담 했을 때 받을 수 있는 금액 Pi
# 상담 최댓값
# 상담 끝나는 날이 N을 넘어가면 안됨
N = int(inp())
T, P = [], []
for _ in range(N):
    t, p = map(int, inp().split())
    T.append(t)
    P.append(p)
dp = [0 for _ in range(N+1)]
for i in range(N):
    for j in range(i + T[i], N+1):
        # 가능한 날짜부터 하나씩 테스트 해보기
        if dp[j] < dp[i] + P[i]:
            dp[j] = dp[i] + P[i]
print(dp[-1])