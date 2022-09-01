import sys
inp = lambda: sys.stdin.readline()
N = int(inp())
A = list(map(int, inp().split()))
for i in range(1, len(A)):
    A[i] += A[i-1]
for _ in range(int(inp())):
    i, j = map(int, inp().split())
    if i == 1:
        print(A[j-1])
    else:
        print(A[j-1]-A[i-2])