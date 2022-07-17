import sys, heapq
inp = sys.stdin.readline
time = sorted([list(map(int, inp().split())) for _ in range(int(inp()))])
res, end_heap = 1, []
heapq.heappush(end_heap, time[0][1])
for s, t in time[1:]:
    if end_heap[0] > s:
        heapq.heappush(end_heap, t)
    else:
        heapq.heappop(end_heap)
        heapq.heappush(end_heap, t)
print(len(end_heap))