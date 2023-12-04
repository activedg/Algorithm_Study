import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
M = int(inp())
nums = list(map(int, inp().split()))
# 양쪽 끝은 차이만큼, 서로 사이는 나누기 2
res = nums[0]
for i in range(M):
    if i == M-1:
        res = max(res, N - nums[i])
    elif i == 0: continue
    else:
        temp = nums[i] - nums[i-1]
        if temp % 2:
            res = max(res, temp // 2 + 1)
        else:
            res = max(res, temp // 2)
print(res)