import sys
inp = lambda : sys.stdin.readline().rstrip()
# 현재 체력 H, 우산 내구도 D
## bfs로 풀시 시간 초과 발생
## 백트래킹? 우산 각각에 대한 다익스트라 후 움직이기
N, H, D = map(int, inp().split())
area = []
start, end, umbrella = [], [], []
## 데이터 전처리
for i in range(N):
    _list = list(inp())
    for j in range(N):
        if _list[j] == 'S':
            start = [i, j]
        elif _list[j] == 'E':
            end = [i, j]
        elif _list[j] == 'U':
            umbrella.append((i, j))
    area.append(_list)
res = sys.maxsize
# 가능한 움직임 다 찾기
## 우산 있는 지점과 종료 지점과 거리 계산하면서 depth, 우산 값 업데이트
def dfs(x, y, hp, u, depth, visiting: list):
    global res
    t = abs(end[0] - x) + abs(end[1] - y)
    ## 곧바로 종료 지점으로 갈 수 있는 경우
    if t <= hp + u:
        res = min(res, depth + t)
    else:
        for k in range(len(umbrella)):
            if not visiting[k]:
                s = abs(umbrella[k][0] - x) + abs(umbrella[k][1] - y)
                if s <= hp + u:
                    visiting[k] = True
                    if s <= u:
                        dfs(umbrella[k][0], umbrella[k][1], hp, D - 1, depth + s, visiting)
                    else:
                        dfs(umbrella[k][0], umbrella[k][1], hp - (s - u - 1), D - 1, depth + s, visiting)
                    visiting[k] = False
dfs(start[0], start[1], H, 0, 0, [False] * len(umbrella))
print(-1) if res == sys.maxsize else print(res)
# q = deque([start])
## bfs로 우선 구현
# while q:
#     x, y, depth, hp, umbrella = q.popleft()
#     ## 체력, 우산 선행 작업
#     if area[x][y] == 'E':
#         print(depth)
#         exit()
#     elif area[x][y] == 'U':
#         umbrella = D - 1
#     elif area[x][y] == '.':
#         if umbrella: umbrella -= 1
#         else: hp -= 1
#
#     if hp:
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < N and 0 <= ny < N and not visiting[nx][ny]:
#                 visiting[nx][ny] = True
#                 q.append((nx, ny, depth + 1, hp, umbrella))
# print(-1)