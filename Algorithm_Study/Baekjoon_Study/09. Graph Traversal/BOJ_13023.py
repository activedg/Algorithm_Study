import sys
from collections import defaultdict
inp = lambda : map(int, sys.stdin.readline().split())
N, M = inp()
friends = defaultdict(list)
## 0, 3/ 3, 2/ 2, 1/ 1, 4
## 0, 4/ 4, 3/ 3, 7/ 7, 1
for _ in range(M):
    a, b = inp()
    friends[a].append(b)
    friends[b].append(a)
friends = dict(sorted(friends.items()))
visited = [False] * (N+1)
def dfs(v, depth):
    if depth == 4:
        print(1)
        exit()
    for f in friends[v]:
        if not visited[f]:
            visited[f] = True
            dfs(f, depth + 1)
            # depth 4 탐색 실패한 경우 False로 다시 초기화
            visited[f] = False
for key in friends.keys():
    visited[key] = True
    dfs(key, 0)
    ## dfs 탐색 실패한 경우 False로 다시 초기화
    visited[key] = False
print(0)