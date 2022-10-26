import sys
sys.setrecursionlimit(10**7)
inp = lambda : sys.stdin.readline()
def dfs(k):
    global team
    visited[k] = True
    path.append(k)
    x = students[k]
    if visited[x]:
        if x in path:
            team += path[path.index(x):]
        return
    else:
        dfs(x)

for _ in range(int(inp())):
    N = int(inp())
    students = [0] + list(map(int, inp().split()))
    # 자기 자신 선택 하면 자기 자신 혼자 팀
    res = 0
    team = []
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            path = []
            dfs(i)
    print(N - len(team))