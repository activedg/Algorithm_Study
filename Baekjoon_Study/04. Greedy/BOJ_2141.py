import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
p = 0
village = sorted([tuple(map(int, inp().split())) for _ in range(N)], key=lambda x:x[0])
p_sum = sum(a for _, a in village)
for x, a in village:
    p += a
    if p >= p_sum / 2:
        print(x)
        exit()