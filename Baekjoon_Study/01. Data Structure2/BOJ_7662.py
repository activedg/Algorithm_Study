import heapq, sys
from collections import defaultdict
for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline())
    max_heap, min_heap = [], []
    counter = defaultdict(int)
    for _ in range(k):
        op, n = sys.stdin.readline().split()
        n = int(n)
        if op == 'I':
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            counter[n] += 1
        else:
            if n == 1:
                while max_heap and not counter[-max_heap[0]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    counter[-max_heap[0]] -= 1
                    heapq.heappop(max_heap)
            else:
                while min_heap and not counter[min_heap[0]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    counter[min_heap[0]] -= 1
                    heapq.heappop(min_heap)
    while max_heap and not counter[-max_heap[0]]:
        heapq.heappop(max_heap)
    while min_heap and not counter[min_heap[0]]:
        heapq.heappop(min_heap)
    print(-max_heap[0], min_heap[0]) if max_heap and min_heap else print('EMPTY')