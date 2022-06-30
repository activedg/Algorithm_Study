import sys, heapq
N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    op = int(sys.stdin.readline())
    if op == 0:
        if not hq:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -op)