import sys
inp = sys.stdin.readline
dp = [[0] * 2001 for _ in range(11)]
dp[0] = [1] * 2001
## Dynamic Programming -> 해당 case 한 번만 계산 하도록
for i in range(1, 11):
    # j 이하의 i개 수를 만드는 방법
    # j를 사용 하고 i개 + j를 사용 하지 않고 i개
    for j in range(1, 2001):
        dp[i][j] = dp[i-1][j//2] + dp[i][j-1]
for _ in range(int(inp())):
    n, m = map(int, inp().split())
    print(dp[n][m])

## dfs 로 정답 맞게 나오나 시간 초과
# def dfs(x, depth, n):
#     if x and depth == n:
#         global res
#         res += 1
#         return
#     elif x == 1 and depth != n:
#         return
#     for i in range(x//3 + 1, x//2 + 1):
#         dfs(i, depth + 1, n)
# for _ in range(int(inp())):
#     n, m = map(int, inp().split())
#     res = 0
#     for t in range(2 ** (n-1), m+1):
#         dfs(t, 1, n)
#     print(res)

