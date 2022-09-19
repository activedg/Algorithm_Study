import sys
from collections import deque
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
know = list(map(int, inp()))
knowing = [False] * (N+1)
true_party = [False] * M
party = []
if not know[0]:
    know = []
else: know = know[1:]
for k in know:
    knowing[k] = True
# 1 5 / 2 6 / 7 / 8 / 7 8 / 9 / 10/ 3 10 / 4
## 1, 2, 3, 4가 포함된 파티를 하는 사람들 전부 아는 사람 처리 해야함
for _ in range(M):
    p = list(map(int, inp()))
    party.append(p[1:])
if not know: print(M)
else:
    q = deque(know)
    while q:
        t = q.popleft()
        for i in range(M):
            if not true_party[i] and t in party[i]:
                true_party[i] = True
                for p1 in party[i]:
                    if p1 != t and not knowing[p1]:
                        q.append(p1)
                        knowing[p1] = True
    print(sum(1 for b in true_party if not b))