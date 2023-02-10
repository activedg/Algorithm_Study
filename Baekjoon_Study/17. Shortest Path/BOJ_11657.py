import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
bus = [[] for _ in range(N+1)]
# 버스 정보 받기
for _ in range(M):
    a, b, c = map(int, inp())
    bus[a].append((b, c))
# 거리 배열
dist = [float("inf") for _ in range(N+1)]
def bf(start):
    dist[start] = 0
    for i in range(N-1):
        for cur_node in range(1, N+1):
            for next_node, dis in bus[cur_node]:
                if dist[cur_node] + dis < dist[next_node]:
                    dist[next_node] = dist[cur_node] + dis
def check_cycle():
    for cur_node in range(1, N+1):
        for next_node, dis in bus[cur_node]:
            if dist[cur_node] + dis < dist[next_node]:
                return True
    return False
bf(1)
if check_cycle():
    print(-1)
else:
    for i in range(2, N+1):
        print(-1 if dist[i] == float("inf") else dist[i])