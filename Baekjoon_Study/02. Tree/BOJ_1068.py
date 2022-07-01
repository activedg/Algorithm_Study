import sys
inp = sys.stdin.readline
N = int(inp())
tree = {}
parents = list(map(int, inp().split()))
del_id = int(inp())
for i in range(N):
    t = parents[i]
    if i == del_id or t == del_id:
        continue
    if t not in tree:
        tree[t] = [i]
    elif i not in tree[t]:
        tree[t].append(i)

cnt = 0
visited = [False] * N
def dfs(val):
    global cnt
    visited[val] = True
    if val not in tree:
        cnt += 1
    else:
        for p in tree[val]:
            if not visited[p]:
                dfs(p)
if -1 in tree:
    dfs(tree[-1][0])
else:
    cnt = 0
print(cnt)


