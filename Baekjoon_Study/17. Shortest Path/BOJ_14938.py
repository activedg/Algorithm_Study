import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
# 낙하산 떨어지는 곳에 아이템 몇 개 있는 지 알려줌
# 수색 범위(m) 내에 가장 많은 아이템 있는 곳
## 양방향 통행 가능
n, m, r = map(int, inp())
items = [0] + list(map(int, inp()))
# 다익스트라 n번
graph = defaultdict(list)
for _ in range(r):
    a, b, c = map(int, inp())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distances = [float("inf") for _ in range(n+1)]
    distances[start] = 0
    q = [(distances[start], start)]
    while q:
        cur_distance, cur_pos = heapq.heappop(q)
        if cur_distance > distances[cur_pos] : continue
        for new_pos, new_distance in graph[cur_pos]:
            distance = cur_distance + new_distance
            if distance < distances[new_pos]:
                distances[new_pos] = distance
                heapq.heappush(q, (distance, new_pos))
    return sum(items[i] for i in range(1, n+1) if distances[i] <= m)

res = 0
for i in range(1, n+1):
    res = max(res, dijkstra(i))
print(res)
# 플로이드 워셜
# dist = [[float("inf") for _ in range(n+1)] for _ in range(n+1)]
# for i in range(1, n+1):
#     dist[i][i] = 0
# # 길의 개수
# for _ in range(r):
#     a, b, c = map(int, inp())
#     dist[a][b] = c
#     dist[b][a] = c
# for k in range(1, n+1):
#     for i in range(1, n+1):
#         if i == k or dist[i][k] == float("inf"): continue
#         for j in range(1, n+1):
#             if dist[i][j] > dist[i][k] + dist[k][j]:
#                 dist[i][j] = dist[i][k] + dist[k][j]
# res = 0
# for i in range(1, n+1):
#     temp = 0
#     for j in range(1, n+1):
#         if dist[i][j] <= m:
#             temp += items[j]
#     res = max(res, temp)
# print(res)