import sys
INF = sys.maxsize
adj = [[0, 5, INF, 9, 1],
       [5, 0, 2, INF, INF],
       [INF, 2, 0, 7, INF],
       [9, INF, 7, 0, 2],
       [1, INF, INF, 2, 0]]
# 인접 행렬을 활용하여 최단 거리 배열인 dist 배열 초기화
dist = [[adj[i][j] for j in range(5)] for i in range(5)]
# 중간 노드가 될 번호를 가장 바깥쪽 for문에 두고 내부 for문에서 로직 수행
for k in range(5):
    for i in range(5):
        for j in range(5):
            if i == j: continue
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
print(dist)