import sys
inp = lambda : sys.stdin.readline().split()
## 위상정렬 배운 후 다시 풀기
N, M = map(int, inp())
dp = [1] * (N + 1)
inp_list = []
for _ in range(M):
    ## a가 b의 선수과목 -> a 이후에 b 들어야 함
    inp_list.append(list(map(int, inp())))
inp_list.sort(key=lambda x: (x[0], x[1]))
for a, b in inp_list:
    temp = dp[a] + 1
    if dp[b] < temp:
        dp[b] = temp
for i in dp[1:]:
    print(i, end=" ")