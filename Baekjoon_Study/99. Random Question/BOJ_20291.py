import sys
from collections import defaultdict
inp = sys.stdin.readline
extends = defaultdict(int)
for _ in range(int(inp())):
    a, b = inp().rstrip().split('.')
    extends[b] += 1
for i in sorted(extends.keys()):
    print(i, extends[i])