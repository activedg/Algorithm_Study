import sys
inp = sys.stdin.readline
n = int(inp())
def gcd(x, y):
    if not y:
        return x
    return gcd(y, x % y)
for _ in range(n):
    a, b = map(int, inp().split())
    print(int(a * b / gcd(a, b)))