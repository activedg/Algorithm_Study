import sys
inp = lambda : int(sys.stdin.readline())
# 자기 좌석 좌우로 자리 옮기기 가능
# VIP 회원은 자기 좌석에만 앉아야 함
N = inp()
## M은 0 이상 N 이하
M = inp()
vip = [False] * (N+1)
## 경우의 수로 풀면 시간 초과 -> 설마 dp?
for _ in range(M):
    vip[inp()] = True
# dp -> i 번째 까지 앉는 경우의 수
dp = [0 for _ in range(N+1)]
dp[0], dp[1] = 1, 1
for i in range(2, N+1):
    if vip[i] or vip[i-1]:
        dp[i] = dp[i-1]
    else:
        # i 번째 사람이 i 번째에 앉는 경우 + i - 1 번째에 앉는 경우
        dp[i] = dp[i-1] + dp[i-2]
print(dp[-1])
# seats = [s for s in range(N+1)]
# ## vip 좌석 번호
# vips = [0] + [inp() for _ in range(M)] + [N+1]
# res = 1
# for i in range(M+1):
#     l, r = vips[i], vips[i+1]
#     seats_temp = seats[l+1:r]
#     temp_perm = permutations(seats_temp)
#     temp_cnt = 0
#     for temp in temp_perm:
#         temp_list = list(temp)
#         check = True
#         for j in range(len(seats_temp)):
#             if abs(temp_list.index(seats_temp[j]) - j) > 1:
#                 check = False
#                 break
#         if check:
#             temp_cnt += 1
#     res *= temp_cnt
# print(res)