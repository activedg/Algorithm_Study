import sys, heapq
inp = lambda : sys.stdin.readline()
N = int(inp())
# 1 2 3 4 -> 19
cards = [int(inp()) for _ in range(N)]
heapq.heapify(cards)
res = 0
while len(cards) >= 2:
    first, second = heapq.heappop(cards), heapq.heappop(cards)
    res += first + second
    heapq.heappush(cards, first+second)
print(res)