# 그래프 알고리즘 - DFS, BFS
많은 양의 데이터 중에서 원하는 데이터를 찾는 과정

## 알아둘 기본적 자료구조
Stack(파이썬에서 기본 list), Queue(파이썬에선 deque)

재귀함수(DFS에 이용될 방식)
: 자기 자신을 다시 호출하는 함수
재귀함수의 종료조건을 명시해야 함

## DFS  
그래프에서 깊은 부분 우선적으로 탐색// 한 우물만 깊게 파기
- 스택 자료구조(혹은 재귀 함수) 이용
- 방문하지 않은 인접노드를 스택에 계속 push -> 해당되는 인접노드가 없는 경우 pop
- 타겟 depth까지 방문 후 판단
- 경우의 수 문제에 적용가능

## BFS 
그래프에서 가까운 노드부터 우선적으로 탐색 // 인접한거 먼저 접근
- 큐 자료구조 이용
- 해당 노드의 인접 노드 중 방문하지 않은 노드 모두 큐에 삽입
- 특정 경로의 최단경로 문제에 효과적으로 적용 가능

## 예시) 백준 13023번 풀이
문제 : 알고리즘 캠프에 N명의 사람이 참가하였는데 A와 B가 친구, B와 C가 친구, C와 D가 친구, D와 E가 친구와 같이 연속되게 친구인 관계가 존재하는지 판단

### 접근 사고
해당하는 경우가 존재하는 지 판단하는 문제라 DFS로 접근하였다. 중요한 포인트는 하나씩 탐색할 때 탐색이 실패한 경우 visited(방문 여부)를 원상 복귀시켜야 또 다른 경우로 진행이 가능하다.
```python
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
```

## 예시) 백준 4179번 풀이
문제 : 미로에서 지훈이가 불 보다 빨리 탈출 할 수 있는지, 그리고 얼마나 빨리 탈출 할 수 있는지 출력하는 문제

### 접근 사고
1분 단위로 지훈이가 한 칸 움직이고 불은 사방으로 퍼져나간다. 1분 단위로 불, 지훈이가 가는 과정을 BFS로 담는다.
불과 지훈 각각 큐를 따로 사용하였으며 불을 먼저 이동 시킨 후 지훈이가 이동 가능한 곳이 있다면 이동시켜 방문여부를 표시하였다.
while q와 같은 반복문의 설정 범위, 분은 어디서 증가시킬지, 큐는 언제까지 pop을 하게 할지가 중요한 문제였다.

```python
import sys
from collections import deque
# BFS 응용 문제
## 최단 시간 문제 -> BFS로 풀이 시작
inp = lambda : sys.stdin.readline().rstrip()
R, C = map(int, inp().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
## 지훈이의 위치에 대한 큐와 불의 위치에 대한 큐
q, fire_q = deque(), deque()
miro = []
for i in range(R):
    t = list(inp())
    miro.append(t)
    for j in range(C):
        if t[j] == 'J':
            q.append((i, j))
        elif t[j] == 'F':
            fire_q.append((i, j))
res = 0
while True:
    # 매 분마다 불, 지훈 이동
    res += 1
    temp = []
    ## 불 먼저 이동
    while fire_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and miro[nx][ny] != '#' and miro[nx][ny] != 'F':
                temp.append((nx, ny))
                miro[nx][ny] = 'F'
    fire_q = deque(temp)
    temp = []
    while q:
        x, y = q.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:
            print(res)
            exit()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < R and -1 < ny < C and miro[nx][ny] == '.':
                temp.append((nx, ny))
                miro[nx][ny] = 'V'
    q = deque(temp)
    if not q: break
print('IMPOSSIBLE')
```


