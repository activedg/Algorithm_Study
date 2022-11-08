import sys
from collections import defaultdict, deque
inp = lambda : map(int, sys.stdin.readline().split())
N, M = inp()
# a, b가 적대 관계/ b, c가 적대 관계 => a, c는 친구 관계
## Todo: 이분 그래프 문제 연습  / 인접한 노드의 visited 값을 계속 -1 곱하기 => visited[o]와 visited[i]가 같으면 리턴 0
## 친구 관계인 두 명을 입력을 받으면 오류
## 적대 관계가 짝수 번으로 이어지면 친구 관계
opponent_list = [[True] * (N+1) for _ in range(N+1)]
opponent_dict = defaultdict(list)
res = 1
for _ in range(M):
    a, b = inp()
    opponent_dict[a].append(b)
    opponent_dict[b].append(a)
visited = [0] * (N+1)
for i in range(1, N+1):
    if not visited[i]:
        q = deque([i])
        visited[i] = 1
        while q:
            x = q.popleft()
            for o in opponent_dict[x]:
                if not visited[o]:
                    visited[o] = -visited[x]
                    q.append(o)
                elif visited[o] == visited[x]:
                    print(0)
                    exit()
print(1)
