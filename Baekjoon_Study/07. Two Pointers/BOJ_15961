import sys
from collections import defaultdict
inp = lambda : sys.stdin.readline()
N, d, k, c = map(int, inp().split())
s = [int(inp()) for _ in range(N)]
## 슬라이딩 윈도우 및 투 포인터를 이용하여 푸는 문제
res = 0
_dict = defaultdict(int)
for i in range(k):
    _dict[s[i]] += 1
l, r = 0, k - 1
while l < N:
    cnt = len(_dict)
    if c not in _dict:
        cnt += 1
    if res < cnt:
        res = cnt
   
    if _dict[s[l]] == 1:
        _dict.pop(s[l])
    else:
        _dict[s[l]] -= 1
    l, r = l + 1, (r + 1) % N
    _dict[s[r]] += 1
print(res)