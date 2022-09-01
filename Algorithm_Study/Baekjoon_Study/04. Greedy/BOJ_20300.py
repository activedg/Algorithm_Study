import sys
inp = sys.stdin.readline
N = int(inp())
T = sorted(list(map(int, inp().split())))
res = 0
if N % 2:
    res = T[-1]
    T.pop()
left, right = 0, len(T)-1
while left < right:
    res = max(res, T[left] + T[right])
    left += 1
    right -= 1
print(res)