import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
# 단백질, 지방, 탄수화물, 비타민
mp, mf, ms, mv = map(int, inp().split())
food = [list(map(int, inp().split())) for _ in range(N)]
## 비용 최소화, 개수 최소화 x
answer, res = [], sys.maxsize
def dfs(k, eat: list, food_list = []):
    global res, answer
    if eat[0] >= mp and eat[1] >= mf and eat[2] >= ms and eat[3] >= mv:
        if eat[4] < res:
            answer = food_list.copy()
            res = eat[4]
        return
    if k == N:
        return
    else:
        for i in range(5):
            eat[i] += food[k][i]
        food_list.append(k + 1)
        dfs(k + 1, eat, food_list)
        for i in range(5):
            eat[i] -= food[k][i]
        food_list.pop()
        dfs(k + 1, eat, food_list)
dfs(0, [0] * 5)
if not answer:
    print(-1)
    exit()
print(res)
print(*answer)