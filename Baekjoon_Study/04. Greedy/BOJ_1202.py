import sys, heapq
inp = lambda : sys.stdin.readline()
N, K = map(int, inp().split())
# 정렬 먼저 진행(그리디 조건 만들기) + 최댓값을 갖고 가는 점에서 heapq 모듈 사용
## 무게 기준으로 정렬
ruby = sorted([tuple(map(int, inp().split())) for _ in range(N)])
bag = [int(inp()) for _ in range(K)]
# 가져갈 수 있는 최대 무게로 가져감
res, i = 0, 0
hq = []
for b in sorted(bag):
    while i < N and ruby[i][0] <= b:
        # bag에서 작은 것 부터 확인
        ## 무게 조건 맞는 것에 대한것 최대힙으로 추가
        heapq.heappush(hq, -ruby[i][1])
        i += 1
    if hq:
        res += -heapq.heappop(hq)
print(res)