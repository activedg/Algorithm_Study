import sys
inp = sys.stdin.readline
N = int(inp())
A = set(map(int, inp().split()))
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if not x%i:
            return False
    return True
res = 1
for a in A:
    if is_prime(a) and a != 1:
        res *= a
print(-1) if res == 1 else print(res)
