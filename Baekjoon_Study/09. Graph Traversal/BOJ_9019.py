import sys
from collections import deque
inp = lambda : sys.stdin.readline()
# D, S, L, R 네가지 명령어 // 레지스터 하나 있음 (0 ~ 9999 값 저장)
## D -> 2n mod 10000
## S -> n - 1 (n이 0인 경우 9999)
## L -> 각 자리수 왼편 회전
## R -> 각 자리수 오른편 회전
# A를 B로 바꾸는 최소한의 명령어
## 가능한 명령어 나열이 여러가지면 아무거나 출력

def bfs(a, b):
    visit = [False] * 10000
    q = deque([(a, '')])
    while q:
        t, op = q.popleft()
        visit[t] = True
        if t == b:
            return op
        for c in ['D', 'S', 'L', 'R']:
            if c == 'D':
                temp = (t * 2) % 10000
                if not visit[temp]:
                    q.append((temp, op + 'D'))
                    visit[temp] = True
            elif c == 'S':
                temp = (t - 1) % 10000
                if not visit[temp]:
                    q.append((temp, op + 'S'))
                    visit[temp] = True
            elif c == 'L':
                ## 1234 -> 2341
                ## 123 -> 1230이 됨
                temp = (t * 10 + t // 1000) % 10000
                if not visit[temp]:
                    q.append((temp, op + 'L'))
                    visit[temp] = True
            else:
                ## 1 -> 1000
                ## 0123 -> 3012
                temp = (t // 10 + (t % 10) * 1000) % 10000
                if not visit[temp]:
                    q.append((temp, op + 'R'))
                    visit[temp] = True

for _ in range(int(inp())):
    A, B = map(int, inp().split())
    print(bfs(A, B))
