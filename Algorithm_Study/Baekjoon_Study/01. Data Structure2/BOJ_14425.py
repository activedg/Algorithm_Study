import sys
N, M = map(int, sys.stdin.readline().split())
s = set()
for i in range(N):
    s.add(sys.stdin.readline().rstrip())
test = [sys.stdin.readline().rstrip() for _ in range(M)]
print(sum(1 for t in test if t in s))
