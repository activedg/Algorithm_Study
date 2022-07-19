import sys
inp = lambda : sys.stdin.readline().split()
N, S = map(int, inp())
num_list = list(map(int, inp()))
i, j = 0, 0
res_sum, res_cnt = 0, N + 1
while True:
    if res_sum >= S:
        res_cnt = min(j-i, res_cnt)
        res_sum -= num_list[i]
        i += 1
    elif j == N: break
    else:
        res_sum += num_list[j]
        j += 1
print(res_cnt) if res_cnt <= N else print(0)
# res_sum, res_cnt = num_list[0], N + 1
# while i < N and j < N:
#     if i > j:
#         j += 1
#     elif res_sum >= S:
#         res_cnt = min(j-i+1, res_cnt)
#         res_sum -= num_list[i]
#         i += 1
#     else:
#         j += 1
#         if j < N: res_sum += num_list[j]
# print(res_cnt) if res_cnt <= N else print(0)

