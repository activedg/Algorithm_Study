import sys
inp = sys.stdin.readline
N, Q = map(int, inp().split())
A = sorted(list(map(int, inp().split())))
for i in range(1, N):
    A[i] += A[i-1]
for _ in range(Q):
    L, R = map(int, inp().split())
    if L > 1:
        print(A[R-1] - A[L-2])
    else:
        print(A[R-1])