import sys
n = int(sys.stdin.readline())
cur = 1
stack, res = [], []
for _ in range(n):
    a = int(sys.stdin.readline())
    while cur <= a:
        stack.append(cur)
        cur += 1
        res.append('+')
    if stack[-1] == a:
        stack.pop()
        res.append('-')
    else:
        res.clear()
        break
if not res:
    print("NO")
else:
    print("\n".join(res))
