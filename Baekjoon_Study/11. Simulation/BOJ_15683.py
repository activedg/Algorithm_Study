import sys, copy
inp = lambda : sys.stdin.readline().split()
## 상하좌우 순서 (0, 1, 2, 3)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cctv_direction = [
    [],
    [[0], [1], [2], [3]],
    [[0, 1], [2, 3]],
    [[0, 3], [1, 3], [1, 2], [0, 2]],
    [[0, 1, 3], [1, 2, 3], [0, 2, 3], [0, 1, 2]],
    [[0, 1, 2, 3]]
]
N, M = map(int, inp())
# 1번은 한 방향(4가지), 2번은 양방향(2가지), 3번은 90도 양방향(4), 4번은 ㅗ세방향(4), 5번은 네방향 전부(1)
## 너무 복잡하게 구현할 문제는 절대 아니다. 케이스 별로 일일이 if문을 쓰고 있다면 무조건 잘못하고 있는거

cctv = []
room = []
res = sys.maxsize
for i in range(N):
    r = list(map(int, inp()))
    for j in range(M):
        if 0 < r[j] < 6:
            cctv.append((i, j, r[j]))
    room.append(r)
def count(graph):
    cnt = 0
    for g in graph:
        cnt += sum(1 for g1 in g if not g1)
    return cnt
def dfs(graph, depth):
    global res, room
    if depth == len(cctv):
        res = min(res, count(graph))
        return
    ## cctv 하나 하나에 대한 dfs
    graph_copy = copy.deepcopy(graph)
    x, y, cctv_type = cctv[depth]
    for d in cctv_direction[cctv_type]:
        watch(x, y, d, graph_copy)
        dfs(graph_copy, depth+1)
        graph_copy = copy.deepcopy(graph)
def watch(x, y, direction, graph):
    for d in direction:
        nx, ny = x, y
        while True:
            nx += move[d][0]
            ny += move[d][1]
            if 0 <= nx < N and 0 <= ny < M:
                if not graph[nx][ny]:
                    graph[nx][ny] = '#'
                elif graph[nx][ny] == 6:
                    break
            else: break
dfs(room, 0)
print(res)