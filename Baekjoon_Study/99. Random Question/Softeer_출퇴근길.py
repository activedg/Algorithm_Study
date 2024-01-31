import sys
from collections import defaultdict, deque
inp = lambda : map(int, sys.stdin.readline().split())
# 출퇴근 겹치는 경우 별로 없음을 알게됨
# 도로 연결 모양, 일방통행 여부
## 단방향 그래프
## 각 동네를 1~n, m개의 일방통행 도로
# S -> T, T->S에 모두 포함될 수 있는 정점의 개수!
# 출근 길 경로에 S 여러 번 등장 가능, 퇴근 길 경로에 T 여러 번 등장 가능
graph = defaultdict(list)
graph_r = defaultdict(list)
n, m = inp()
for _ in range(m):
    x, y = inp()
    graph[x].append(y)
    graph_r[y].append(x)
S, T = inp()
# 1 -> 4 -> 3 경로에서 4가 공통 정점 일려면 3 -> 4 -> 1도 가능해야 함 => 반대 방향 그래프도 있어야함
def bfs(cur, g, visit):
    q = deque([cur])
    visit.add(cur)
    while q:
        temp = q.popleft()
        for node in g[temp]:
            if node not in visit:
                visit.add(node)
                q.append(node)
fromS = set()
fromS.add(T)
bfs(S, graph, fromS)

fromT = set()
fromT.add(S)
bfs(T, graph, fromT)

toS = set()
bfs(S, graph_r, toS)

toT = set()
bfs(T, graph_r, toT)

res = fromS & fromT & toS & toT
print(len(res) - 2)