# import sys
# inp = lambda : sys.stdin.readline().split()
# # 학교에 가기 위해 D킬로 고속도로
# # 모든 지름길 일방통행, 고속도로 역주행 불가
# N, D = map(int, inp())
# ## 지름길 시작 위치, 도착위치, 지름길의 길이
# shortcuts = [list(map(int, inp())) for _ in range(N)]
# shortcuts.sort()
# # 운전해야 하는 거리의 최솟값
# dp = [i for i in range(10001)]
# # 0 10 9/ 10 50 40/ 50 70 15/ 70 140 70/140 180 28/ 450/0
# # 9 40 15 70 28 270
# end_list = []
# for i in range(N):
#     start, end, cost = shortcuts[i][0], shortcuts[i][1], shortcuts[i][2]
#     for e in end_list:
#         if start > e:
#             dp[start] = min(dp[e] + start - e, dp[start])
#     dp[end] = min(dp[start] + cost, dp[end])
#     if end < D:
#         dp[D] = min(dp[D], dp[end] + (D - end))
#     end_list.append(end)
# print(dp[D])

import sys
inp = lambda : sys.stdin.readline().split()
N, D = map(int, inp())
dp = [i for i in range(D+1)]
shortcuts = [[] for _ in range(D+1)]
for _ in range(N):
    start, end, cost = map(int, inp())
    if end <= D:
        shortcuts[end].append((start, cost))
for i in range(2, D+1):
    if shortcuts[i]:
        temp = min([dp[s] + c for s, c in shortcuts[i]])
        dp[i] = min(dp[i-1] + 1, temp)
    else:
        dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[D])
# distances = [i for i in range(D+1)]
# shortcuts = [list(map(int, inp())) for _ in range(N)]
#
# for i in range(D+1):
#     distances[i] = min(distances[i-1] + 1, distances[i])
#     for start, end, cost in shortcuts:
#         if i == start and end <=D and distances[i] + cost < distances[end]:
#             distances[end] = distances[i] + cost
# print(distances[-1])