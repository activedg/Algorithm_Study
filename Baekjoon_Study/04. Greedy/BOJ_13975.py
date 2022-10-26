import sys, heapq
inp = lambda : sys.stdin.readline()
for _ in range(int(inp())):
    N = int(inp())
    # heapq 사용하여 항상 최솟값 두 개 pop하기
    ## 합치고 난 후에 push
    files = list(map(int, inp().split()))
    heapq.heapify(files)
    cost = 0
    while len(files) >= 2:
        cost1 = heapq.heappop(files)
        cost2 = heapq.heappop(files)
        cost += cost1 + cost2
        heapq.heappush(files, cost1 + cost2)
    print(cost)
