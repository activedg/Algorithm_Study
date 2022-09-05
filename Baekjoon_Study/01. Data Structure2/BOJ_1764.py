import sys
from collections import defaultdict
## 해시 구조 혹은 set 구조로 푸는 문제
inp = lambda : sys.stdin.readline().rstrip()
N, M = map(int, inp().split())
# never = defaultdict(int)
# for _ in range(N):
#     never[inp()] += 1
# res = []
# for _ in range(M):
#     t = inp()
#     if never[t] == 1:
#         res.append(t)
# print(len(res))
# for r in sorted(res):
#     print(r)
nameList = sys.stdin.read().splitlines()
heard_set = set(nameList[:N])
seen_set = set(nameList[N:])
res = list(heard_set&seen_set)
print(len(res))
for r in sorted(res):
    print(r)