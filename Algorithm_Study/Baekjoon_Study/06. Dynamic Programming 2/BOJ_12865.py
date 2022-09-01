import sys
## 아직 미완성
inp = lambda : sys.stdin.readline().split()
N, K = map(int, inp())
items = []
for _ in range(N):
    items.append(list(map(int, inp())))
items.sort(key=lambda x: x[0])
print(items)