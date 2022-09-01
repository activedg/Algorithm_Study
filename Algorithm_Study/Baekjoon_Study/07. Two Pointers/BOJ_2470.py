import sys
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
sol = sorted(list(map(int, inp().split())))
l, r = 0, N - 1
res = [sol[l] + sol[r], l, r]
while l < r:
    temp = sol[l] + sol[r]
    if abs(temp) < abs(res[0]):
        res = [temp, l, r]
        
    if temp < 0:
        l += 1
    else:
        r -= 1
print(sol[res[1]], sol[res[2]])