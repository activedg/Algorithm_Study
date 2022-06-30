import sys
inp = sys.stdin.readline
s = inp().rstrip()
d = {}
cnt = 0
while s:
    if s in d: d[s] += 1
    else: d[s] = 1
    cnt += 1
    s = inp().rstrip()
d = sorted(d.items())
for key, value in d:
    res = value * 100 / cnt
    print(key, "{0:.4f}".format(res))