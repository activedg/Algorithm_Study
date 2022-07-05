import sys
inp = sys.stdin.readline
rope = [int(inp()) for _ in range(int(inp()))]
res = 0
for i, r in enumerate(sorted(rope, reverse=True)):
    r *= i + 1
    if res < r: res = r
print(res)