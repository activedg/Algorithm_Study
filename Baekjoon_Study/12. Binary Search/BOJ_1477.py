import sys
inp = lambda : sys.stdin.readline().split()
# 휴게소 M개 더 세우기
# 이미 휴게소가 있는 곳에 세울 수 x, 끝에도 불가, 정수 위치에만!
# 모든 휴게소 방문 -> 휴게소가 없는 구간의 길이의 최댓값을 최소로
N, M, L = map(int, inp())
rests = [0] + sorted(map(int, inp())) + [L]
# 현재 최댓값 -> end
dist = []
for i in range(1, len(rests)):
    dist.append(rests[i] - rests[i-1])
# end값 L-1이어도 됨
start, end = 1, max(dist)
res = end
while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for i in range(len(dist)):
        if dist[i] > mid:
            cnt += (dist[i] - 1) // mid
    if cnt > M:
        start = mid + 1
    else:
        end = mid - 1
        # cnt가 부족한 경우 남는 아무 곳에나 넣어도 되기 때문에 res값을 매번 갱신해준다.
        res = mid
print(res)