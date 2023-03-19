import sys
inp = lambda : sys.stdin.readline().rstrip()
# 파이프는 건물이 잇으면 설치 못함
# 첫째 열 -> 마지막 열로 가야함
## 최대한 같은 행으로 움직이 돼 못 움직이면 다음 행으로 움직이기
R, C = map(int, inp().split())
roads = [list(inp()) for _ in range(R)]
dx = [-1, 0, 1]
def dfs(x, y):
    roads[x][y] = 'p'
    # 마지막 행 도달
    if y == C-1: return True
    for i in range(3):
        nx = x + dx[i]
        ny = y + 1
        if 0 <= nx < R and roads[nx][ny] == '.':
            # return 값이 False일 때 roads 값 원상 복귀 할 필요 x -> 다시 가도 못 가는 루트임
            if dfs(nx, ny):
                return True
    return False
res = 0
for i in range(R):
    if dfs(i, 0):
        res += 1
print(res)