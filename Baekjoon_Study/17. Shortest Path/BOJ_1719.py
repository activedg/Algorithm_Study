import sys, heapq
from collections import defaultdict
INF = float("inf")
inp = lambda: sys.stdin.readline().split()
n, m = map(int, inp())
# 다른 경로 거쳐가는 경우 그 경로로 업데이트
# def floyd_warshall():
#     dist = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
#     route = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#     for _ in range(m):
#         a, b, c = map(int, inp())
#         if dist[a][b] > c:
#             dist[a][b] = c
#             dist[b][a] = c
#             route[b][a] = a
#             route[a][b] = b
#     # 플로이드 워셜
#     ## 1 -> 6 으로 가려면 1 -> 2-> 5 -> 2이지만 1과 5는 connected x
#     for k in range(1, n+1):
#         for i in range(1, n+1):
#             if i == k or dist[i][k] == INF: continue
#             for j in range(1, n+1):
#                 if i == j: continue
#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#                     route[i][j] = route[i][k]
#     for i in range(1, n+1):
#         print(' '.join('-' if route[i][j] == 0 else str(route[i][j]) for j in range(1, n+1)))
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, inp())
    graph[a].append((b, c))
    graph[b].append((a, c))
def dijkstra(start):
    dist = [float("inf") for _ in range(n+1)]
    # 직전 노드 저장
    prev = [0 for _ in range(n+1)]
    dist[start] = 0
    q = [(dist[start], start)]
    while q:
        cur_distance, cur_pos = heapq.heappop(q)
        if cur_distance > dist[cur_pos]: continue
        for new_pos, new_distance in graph[cur_pos]:
            distance = new_distance + cur_distance
            if distance < dist[new_pos]:
                dist[new_pos] = distance
                # 직전 노드 번호 갱신
                prev[new_pos] = cur_pos
                heapq.heappush(q, (distance, new_pos))
    for i in range(1, n+1):
        if i == start:
            print("-", end=' ')
        elif prev[i] == start:
            print(i, end =' ')
        else:
            temp = i
            while True:
                if prev[temp] == start:
                    print(temp, end =' ')
                    break
                else:
                    temp = prev[temp]
for i in range(1, n+1):
    dijkstra(i)
    print()