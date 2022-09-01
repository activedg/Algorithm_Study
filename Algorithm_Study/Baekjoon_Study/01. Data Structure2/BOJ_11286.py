import sys, heapq
inp = sys.stdin.readline
N = int(inp())
# heapq 두개 이용
hp = []
hn = []
for _ in range(N):
    op = int(inp())
    if op == 0:
        if hp and hn:
            if hp[0] < hn[0]:
                print(heapq.heappop(hp))
            else:
                print(-heapq.heappop(hn))
        elif hp:
            print(heapq.heappop(hp))
        elif hn:
            print(-heapq.heappop(hn))
        else:
            print(0)
    else:
        if op > 0:
            heapq.heappush(hp, op)
        else:
            heapq.heappush(hn, -op)