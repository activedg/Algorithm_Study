import sys
inp = lambda: sys.stdin.readline()
N = int(inp())
board = [list(map(int, inp().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
      if i == N-1 and j == N-1: break
      r = i + board[i][j]
      c = j + board[i][j]
      if r < N: dp[r][j] += dp[i][j]
      if c < N: dp[i][c] += dp[i][j]
print(dp[N-1][N-1])
