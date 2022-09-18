from collections import Counter
import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
# count = Counter(sorted(map(int, inp())))
# res = []
# def dfs(k):
#     if k == M:
#         print(*res)
#         return
#     for num in count.keys():
#         if count[num]:
#             res.append(num)
#             count[num] -= 1
#             dfs(k+1)
#             res.pop()
#             count[num] += 1
# dfs(0)
## Counter 사용 안하는 방법
## buffer와 visited를 사용하여 중복된 값 dfs로 요청하지 않도록 하기
res = []
num = sorted(map(int, inp()))
visited = [False] * N
def dfs(k):
    if k == M:
        print(*res)
        return
    buffer = 0
    for i in range(N):
        if not visited[i] and buffer != num[i]:
            visited[i] = True
            res.append(num[i])
            buffer = num[i]
            dfs(k+1)
            res.pop()
            visited[i] = False
dfs(0)