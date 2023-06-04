import sys, heapq
from collections import defaultdict
inp = lambda : sys.stdin.readline().split()
# 집들 사이에 총 M개의 양방향 도로
# 하루에 X보다 먼 거리 걷지 않고 거리가 가까운 집부터
# 왕복할 수 없는 거리는 다음날로
N, M, X, Y = map(int, inp())
# Y에서 부터 발생하는 모든 간선에 대해 다익스트라
graph = defaultdict(list)
for _ in range(M):
    a, b, c = map(int, inp())
    graph[a].append((b, c))
    graph[b].append((a, c))
# Y부터 출발하는 distances
distances = [float("inf") for _ in range(N)]
distances[Y] = 0
hq = [(0, Y)]
while hq:
    cur_distance, cur_pos = heapq.heappop(hq)
    if distances[cur_pos] < cur_distance: continue
    for new_pos, new_distance in graph[cur_pos]:
        distance = cur_distance + new_distance
        if distance < distances[new_pos]:
            distances[new_pos] = distance
            heapq.heappush(hq, (distance, new_pos))
# 거리 리스트 정렬
distances.sort()
# 자기 집(Y) 빼기
i, res = 1, 0
while i < N:
    temp = 0
    while temp <= X and i < N:
        temp += distances[i] * 2
        if temp <= X: i += 1
    res += 1
    if i < N and distances[i] * 2 > X:
        res = -1
        break

print(res)