import sys
from collections import defaultdict
inp = lambda : sys.stdin.readline()
N, H = map(int, inp().split())
def_dict = defaultdict(int)
top, down = [], []
for i in range(N):
    if i % 2:
        top.append(int(inp()))
    else:
        down.append(int(inp()))
top.sort()
down.sort()
left, right = 1, H
min_cnt = 2000001
while left < right:
    left_cnt, right_cnt = 0, 0
    for i in range(N//2):
        if left <= down[i]:
            left_cnt += 1
        if left > H - top[i]:
            left_cnt += 1
        left += 1
        def_dict[left_cnt] += 1
        if H - right <= top[i]:
            right_cnt += 1
        if down[i] < right:
            right_cnt += 1
        right -= 1
        def_dict[right_cnt] += 1
print(def_dict)
