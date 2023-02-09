import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
# A -> B말고도 다른 곳 거쳐갈 수 있음 => 플로이드 워셜
# C시간 뒤에 B번 파티장에서 파티 열림
roads = [list(map(int, inp())) for _ in range(N)]
for k in range(N):
    for i in range(N):
        if i == k: continue
        for j in range(N):
            if i == j: continue
            if roads[i][j] > roads[i][k] + roads[k][j]:
                roads[i][j] = roads[i][k] + roads[k][j]
for _ in range(M):
    a, b, c = map(int, inp())
    print("Enjoy other party") if roads[a-1][b-1] <= c else print("Stay here")