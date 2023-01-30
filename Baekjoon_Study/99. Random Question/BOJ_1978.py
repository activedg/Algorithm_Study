import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
arr = list(map(int, inp().split()))
cnt = 0
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True
for x in arr:
    if is_prime(x):
        cnt += 1
print(cnt)