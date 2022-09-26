from collections import defaultdict, deque
import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
_dict = defaultdict(set)
for _ in range(M):
    x, y = map(int, inp())
    _dict[x].add(y)
    _dict[y].add(x)
S, E = map(int, inp())
def bfs(start, end, path_temp: list):
    res = [sys.maxsize, []]
    ## path로 경로 확인?
    q = deque([(start, 0, path_temp)])
    visited = defaultdict(int)
    for p in path_temp:
        visited[p] += 1
    while q:
        t, depth, path = q.popleft()
        if t == end:
            if res[0] > depth:
                res = [depth, [path]]
            elif res[0] == depth:
                res[1].append(path)
        else:
            ## 가지 않은 정점으로 가는 것
            for d in _dict[t]:
                if not visited[d]:
                    visited[d] += 1
                    q.append((d, depth+1, path + [d]))
    return [res[0], sorted(res[1])[0]]
temp = bfs(S, E, [S])
temp[1].remove(S)
print(temp[0] + bfs(E, S, temp[1])[0])