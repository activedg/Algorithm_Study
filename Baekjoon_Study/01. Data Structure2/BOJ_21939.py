import sys, heapq
from collections import defaultdict
N = int(sys.stdin.readline())
he, hh = [], []
def_dict = defaultdict(bool)
for _ in range(N):
    p, l = map(int, sys.stdin.readline().split())
    heapq.heappush(he, (l, p))
    heapq.heappush(hh, (-l, -p))
    def_dict[p] = True
M = int(sys.stdin.readline())
for _ in range(M):
    temp = sys.stdin.readline().split()
    if temp[0] == 'recommend':
        x = int(temp[1])
        if x == 1:
            while not def_dict[-hh[0][1]]:
                heapq.heappop(hh)
            print(-hh[0][1])
        else:
            while not def_dict[he[0][1]]:
                heapq.heappop(he)
            print(he[0][1])
    elif temp[0] == 'add':
        p, l = int(temp[1]), int(temp[2])
        def_dict[p] = True
        heapq.heappush(he, (l, p))
        heapq.heappush(hh, (-l, -p))
    elif temp[0] == 'solved':
        def_dict[int(temp[1])] = False
        while not def_dict[he[0][1]]:
            heapq.heappop(he)
        while not def_dict[-hh[0][1]]:
            heapq.heappop(hh)
