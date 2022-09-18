import sys
from collections import Counter
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
trees = Counter(map(int, inp()))
## 20/ 4 26 40 42 46
### Counter를 사용하여 중복된 숫자 연산 감소
res = 0
def search(start, end):
    global res
    if start > end:
        return
    mid = (start + end) // 2
    cut_sum = sum((t - mid) * cnt for t, cnt in trees.items() if t > mid)
    if cut_sum >= M:
        res = mid
        search(mid+1, end)
    else:
        search(start, mid-1)
search(0, max(trees))
print(res)