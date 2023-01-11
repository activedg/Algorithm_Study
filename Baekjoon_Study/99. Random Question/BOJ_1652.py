import sys
inp = lambda : sys.stdin.readline()
# 2칸 이상 누울 수 있으면 count
N = int(inp())
room = [list(inp()) for _ in range(N)]
r_cnt, c_cnt = 0, 0
for i in range(N):
    temp = 0
    for j in range(N):
        if room[i][j] == '.':
            temp += 1
            if j == N-1 and temp >= 2:
                r_cnt += 1
        else:
            # room[i][j]가 X일 떄
            if temp >= 2:
                r_cnt += 1
            temp = 0
for j in range(N):
    temp = 0
    for i in range(N):
        if room[i][j] == '.':
            temp += 1
            if i == N-1 and temp >= 2:
                c_cnt += 1
        else:
            # room[i][j]가 X일 떄
            if temp >= 2:
                c_cnt += 1
            temp = 0
print(r_cnt, c_cnt)