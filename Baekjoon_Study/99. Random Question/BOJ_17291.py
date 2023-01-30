import sys
inp = lambda : int(sys.stdin.readline())
# 1년 2월에 1마리 탄생
# 매년 1월이 되면 분열, 본래 개체 존재, 새로운 개체 하나 탄생
# 홀수년도에 탄생 -> 3번 분열시 사망, 짝수년도 -> 4번 분열 시 사망
dp = [[0] * 4 for _ in range(21)]
# i년에 j년차인 벌레 개수 => dp[i][j]
dp[1][0] = 1
for i in range(2, 21):
    for j in range(1, 4):
        dp[i][j] += dp[i-1][j-1]
        dp[i][0] += dp[i-1][j-1]
