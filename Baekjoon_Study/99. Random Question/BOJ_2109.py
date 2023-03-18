import sys, heapq
inp = lambda : sys.stdin.readline()
# d 일안에 와서 해주면 p만큼 강연료
# 하루에 한 곳만 가능
n = int(inp())
## 5
## 3 3
## 2 3
## 1 3
## 100 4
## 90 4
lecture = [list(map(int, inp().split())) for _ in range(n)]
lecture.sort(key=lambda x:x[1])
hq = []
for money, day in lecture:
    # 돈 기준으로 일단 다 heapq에 넣음
    heapq.heappush(hq, money)
    # 힙큐의 길이가 day 보다 커진 경우, 즉 마감일을 넘긴 경우 가장 돈을 적게 주는 걸 드랍
    if len(hq) > day:
        heapq.heappop(hq)
print(sum(hq))