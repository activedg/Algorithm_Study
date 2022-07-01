import sys
inp = sys.stdin.readline
k = int(inp())
res = [[] for _ in range(k)]
tree = list(map(int, inp().split()))
def inorder(t, depth):
    if len(t) == 1:
        res[depth].extend(t)
        return
    mid = len(t) // 2
    res[depth].append(t[mid])
    inorder(t[:mid], depth+1)
    inorder(t[mid+1:], depth+1)

inorder(tree, 0)
for i in range(k):
    print(*res[i])
