import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
N, M, X = map(int, inp())
## 다익스트라 공부 필수
def dijkstra(start, distances: list, g: defaultdict(dict)):
    distances[start] = 0
    hq = []
    heapq.heappush(hq, (distances[start], start))
    while hq:
        cur_distance, cur_node = heapq.heappop(hq)
        if distances[cur_node] < cur_distance: continue
        for new_node, new_distance in g[cur_node].items():
            ## cur_distance + new_distance 와 비교
            distance = cur_distance + new_distance
            if distance < distances[new_node]:
                distances[new_node] = distance
                heapq.heappush(hq, (distance, new_node))
res = 0
graph = defaultdict(dict)
## 역방향 그래프 정하기
graph_r = defaultdict(dict)
for _ in range(M):
    a, b, c = map(int, inp())
    graph[a][b] = c
    graph_r[b][a] = c
dist = [sys.maxsize] * (N+1)
dist_r = [sys.maxsize] * (N+1)
dijkstra(X, dist, graph)
dijkstra(X, dist_r, graph_r)
for i in range(1, N+1):
    res = max(res, dist[i] + dist_r[i])
print(res)