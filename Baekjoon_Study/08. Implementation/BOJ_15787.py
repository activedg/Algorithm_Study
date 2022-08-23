import sys
inp = lambda : map(int, sys.stdin.readline().split())
N, M = inp()
trains = [[0] * 20 for _ in range(N)]
temp = []
for _ in range(M):
    op = list(inp())
    if op[0] == 1:
        trains[op[1]-1][op[2]-1] = 1
    elif op[0] == 2:
        trains[op[1]-1][op[2]-1] = 0
    elif op[0] == 3:
        del trains[op[1]-1][-1]
        a = [0]
        a.extend(trains[op[1]-1])
        trains[op[1]-1] = a
    elif op[0] == 4:
        del trains[op[1]-1][0]
        trains[op[1]-1].extend([0])
for t in trains:
    if not temp:
        temp.append(t)
    else:
        if t not in temp: temp.append(t)
print(len(temp))

# elif op[0] == 3:
# for i in range(19, 0, -1):
#     trains[op[1] - 1][i] = trains[op[1] - 1][i - 1]
# trains[op[1] - 1][0] = 0
# elif op[0] == 4:
# for i in range(19):
#     trains[op[1] - 1][i] = trains[op[1] - 1][i + 1]
# trains[op[1] - 1][19] = 0