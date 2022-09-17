import sys
inp = lambda : sys.stdin.readline().rstrip()
n, m = map(int, inp().split())
square = [[0] * (m+1) for _ in range(n+1)]
for i in range(n):
    t = list(inp())
    for j in range(m):
        square[i+1][j+1] = int(t[j])
res_max = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if square[i][j]:
            square[i][j] = min(square[i][j-1], square[i-1][j-1], square[i-1][j]) + 1
            res_max = max(res_max, square[i][j])
print(int(pow(res_max, 2)))