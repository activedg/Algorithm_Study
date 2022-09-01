import sys
inp = lambda : map(int, sys.stdin.readline().split())
N, K = inp()
a = list(inp())
cnt = [0] * (max(a) + 1)
left, right, res = 0, 0, 0
while right < N:
    if cnt[a[right]] < K:
        cnt[a[right]] += 1
        right += 1
        res = max(right - left, res)
    else:
        cnt[a[left]] -= 1
        left += 1
print(res)