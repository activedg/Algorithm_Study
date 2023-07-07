import sys
inp = lambda : sys.stdin.readline()
# 마지막 두 숫자 사이에 '=', 나머지 숫자 사이에는 '+', '-' 넣기
# 중간에 나오는 수가 모두 0이상 20 이하이어야 함
N = int(inp())
nums = list(map(int, inp().split()))
# 2차원 dp 배열 만들기
dp = [[0 for _ in range(21)] for _ in range(N-1)]
dp[0][nums[0]] = 1
# 첫번째 원소부터 N-2번째 까지
for i in range(N-2):
    # i-1번째 dp 중 경우의 수 존재하는 경우만 체크
    for j in range(21):
        if not dp[i][j]: continue

        temp_1, temp_2 = j + nums[i+1], j - nums[i+1]

        if temp_1 <= 20:
            dp[i+1][temp_1] += dp[i][j]
        if temp_2 >= 0:
            dp[i+1][temp_2] += dp[i][j]

print(dp[-1][nums[-1]])