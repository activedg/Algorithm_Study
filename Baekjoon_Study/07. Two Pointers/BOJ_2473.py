import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
fill = sorted(map(int, inp().split()))
# 특성 값이 가장 0에 가까운 세 용액 찾기
## -97 -6 -2 6 98
res = [sys.maxsize, (0, 0, 0)]
for i in range(N):
    ## 쓰리 포인터 / for 문으로 돌면서 s, e 값 변경 하면서 탐색
    s, e = i+1, N-1
    target = -fill[i]
    while s < e:
        two_sum = fill[s] + fill[e]
        if abs(two_sum - target) < res[0]:
            res[0] = abs(two_sum - target)
            res[1] = (fill[i], fill[s], fill[e])
        if two_sum < target:
            s += 1
        elif two_sum > target:
            e -= 1
        else:
            print(*res[1])
            exit()
print(*res[1])