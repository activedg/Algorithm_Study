import sys
inp = sys.stdin.readline
N = int(inp())
line = inp().rstrip()
cnt = {'B': 0, 'R': 0}
cnt[line[0]] += 1
for i in range(1, N):
    if line[i] != line[i-1]:
        cnt[line[i]] += 1
print(min(cnt.values())+1)