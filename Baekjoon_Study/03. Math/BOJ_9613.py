import sys
inp = sys.stdin.readline
def gcd(a, b):
    if not b: return a
    return gcd(b, a % b)
t = int(inp())
for _ in range(t):
    test = list(map(int, inp().split()))
    n, test = test[0], test[1:]
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res += gcd(test[i], test[j])
    print(res)