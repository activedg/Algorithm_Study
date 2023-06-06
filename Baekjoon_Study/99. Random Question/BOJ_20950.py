import sys
from itertools import combinations
inp = lambda : sys.stdin.readline()
# 남은 물감 섞어 곰두리색 물감 단들기
# 혼합 할 모든 물감의 R, G, B값 더하고 물감의 개수로 나누기
# 물감들을 섞어서 만들 수 있는 색 중 가장 곰두리색에 가까운 색이 문두리색
# 최대 7개까지 색만 혼합 가능
N = int(inp())
# 물감 색들
colors = [list(map(int, inp().split())) for _ in range(N)]
# 곰두리색
target = list(map(int, inp().split()))
# 컴비네이션으로 구하돼, 최대 7개까지만 가능
# index 배열 만들기
indices = [i for i in range(N)]
# 2개 선택부터 N개 선택까지 구하기
res = sys.maxsize
# for num in range(2, min(7, N) + 1):
#     for comb in combinations(indices, num):
#         temp = [0, 0, 0]
#         for i in list(comb):
#             for j in range(3):
#                 temp[j] += colors[i][j]
#         temp_res = 0
#         for j in range(3):
#             temp[j] = temp[j] // len(comb)
#             temp_res += abs(target[j] - temp[j])
#         res = min(res, temp_res)
# print(res)
def dfs(index, depth, r, g, b):
    if depth > 1:
        global res
        res = min(res, abs(target[0] - r // depth) + abs(target[1] - g // depth) + abs(target[2] - b // depth))

    if depth == 7 or depth == N:
        return

    for i in range(index, N):
        dfs(i+1, depth + 1, r + colors[i][0], g + colors[i][1], b + colors[i][2])
dfs(0, 0, 0, 0, 0)
print(res)