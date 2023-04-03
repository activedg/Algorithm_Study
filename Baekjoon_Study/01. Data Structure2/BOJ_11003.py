import sys, heapq
from collections import deque
inp = lambda : sys.stdin.readline().split()
N, L = map(int, inp())
## 12 3
## 1 5 2 3 6 2 3 7 3 5 2 6
### 1 1 1 2 2 2 2 2 3 3 2 2
A = list(map(int, inp()))
# i-L+1 번째 A부터 i번째 A까지의 최솟값
# 해당 index가 0보다 작으면 패스
## 리스트에서 L - 1 전까지 탐색
q = deque()
D = [0] * N
for i in range(N):
    # 힙에서 원소를 추가하고 제거할 때 log(n)의 시간 걸 => 덱으로 항상 첫 원소가 최소가 되도록 바꿔보자!
    ## 덱으로 최소 힙 구현해보기

    # 현재 A값 보다 q의 마지막 원소가 크거나 같을 때
    ## 덱의 마지막 원소를 계속 확인하여 현재 A값 보다 크면 덱에서 제거
    while q and q[-1][0] > A[i]:
        q.pop()

    # 최솟값이 구하고자 하는 범위 밖의 인덱스의 원소일 때
    while q and q[0][1] <= i - L:
        q.popleft()
    q.append((A[i], i))

    D[i] = q[0][0]
    # heapq.heappush(hq, (A[i], i))
    # while hq and hq[0][1] <= i - L:
    #     heapq.heappop(hq)
    # D[i] = hq[0][0]
print(*D)