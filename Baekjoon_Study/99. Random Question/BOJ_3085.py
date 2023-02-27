import sys
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
candy = [list(inp()) for _ in range(N)]
res = 1
# 사탕 색이 다른 인접한 두 칸 고르기 -> 서로 교환 -> 가장 긴 연속 부분(행 또는 열) 고르고 먹기
def candy_count():
    global res
    for i in range(N):
        # 각 행 먼저 판별
        cnt = 1
        for j in range(1, N):
            if candy[i][j-1] == candy[i][j]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
    for j in range(N):
        # 각 열 판별
        cnt = 1
        for i in range(1, N):
            if candy[i][j] == candy[i-1][j]:
                cnt += 1
                res = max(res, cnt)
            else:
                cnt = 1
candy_count()
for i in range(N):
    for j in range(N):
        # 우측 으로만 교환
        if j + 1 < N and candy[i][j] != candy[i][j+1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            candy_count()
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        if i + 1 < N and candy[i][j] != candy[i+1][j]:
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
            candy_count()
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]
print(res)