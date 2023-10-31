import sys, heapq
inp = lambda : sys.stdin.readline()
N = int(inp())
hq = []
for _ in range(N):
    temp = list(map(int, inp().split()))
    # 길이가 N인 최소힙
    for t in temp:
        if len(hq) < N:
            heapq.heappush(hq, t)
        else:
            # 최소힙에서 맨 앞에 있는 원소보다 t가 더 큼
            if hq[0] < t:
                # heapq.heappop(hq)
                # heapq.heappush(hq, t)
                heapq.heapreplace(hq, t)
print(hq[0])
# nums = []
# for _ in range(N):
#     temp = list(map(int, inp().split()))
#     for t in temp:
#         nums.append(t)
# print(sorted(nums, reverse=True)[N-1])