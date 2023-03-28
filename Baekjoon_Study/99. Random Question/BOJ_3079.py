import sys
inp = lambda : sys.stdin.readline().rstrip()
N, M = map(int, inp().split())
times = [int(inp()) for _ in range(N)]
# 입국 심사대 N개, 총 M명의 사람 지나감
# 총 걸리는 시간을 매개 변수로 -> 해당 매개 변수에 M명 통과 가능 한지
start, end = 0, min(times) * M
## 2 6
## 7 10
res = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for t in times:
        cnt += mid // t
        if cnt >= M: break
    if cnt < M:
        start = mid + 1
    else:
        res = mid
        end = mid - 1
print(res)
## 7 10
## 2 3 3 4 6 8 9
## 2 3 3