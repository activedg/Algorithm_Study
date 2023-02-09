import sys
INF = sys.maxsize
inp = lambda : sys.stdin.readline()
# n개의 도시, m개의 버스 / 버스 한 번 사용할 때 마다 비용
## 도시 i 에서 j로 가는데 필요한 최소 비용
n = int(inp())
m = int(inp())
bus = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    bus[i][i] = 0
# 노선이 하나가 아닐 수도 있음
for _ in range(m):
    a, b, c = map(int, inp().split())
    # 버스 노선이 기존에 존재하는 경우
    if c < bus[a][b]:
        bus[a][b] = c
# 플로이드 - 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        if i == k or bus[i][k] == INF: continue
        for j in range(1, n+1):
            if i == j: continue
            if bus[i][k] + bus[k][j] < bus[i][j]:
                bus[i][j] = bus[i][k] + bus[k][j]
# i 에서 j로 갈 수 없는 경우 0 출력
for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == INF:
            bus[i][j] = 0
        print(bus[i][j], end=' ')
    print()