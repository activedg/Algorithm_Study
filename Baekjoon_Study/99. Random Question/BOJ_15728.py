import sys
inp = lambda : map(int, sys.stdin.readline().split())
N, K = inp()
shared = list(inp())
team = list(inp())
for _ in range(K+1):
    temp_max = [-sys.maxsize, 0]
    for i in range(len(shared)):
        for j in range(len(team)):
            if temp_max[0] < shared[i] * team[j]:
                temp_max = [shared[i] * team[j], j]
    if _ < K : del team[temp_max[1]]
    else : print(temp_max[0])