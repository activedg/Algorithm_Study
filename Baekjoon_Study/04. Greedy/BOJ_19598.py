import sys, heapq
inp = lambda : sys.stdin.readline()
# 그리디 알고리즘 + 정렬 후 최소 힙에 넣고 조건 비교 하고 최솟값 찾기)
## x[0] 값에 따른 정렬된 순서 -> 최적의 해 찾을 수 있는 조건
N = int(inp())
time = [list(map(int, inp().split())) for _ in range(N)]
time.sort(key=lambda x:x[0])
hq = []
for s, e in time:
    if hq and hq[0] <= s:
        heapq.heappop(hq)
    heapq.heappush(hq, e)
print(len(hq))