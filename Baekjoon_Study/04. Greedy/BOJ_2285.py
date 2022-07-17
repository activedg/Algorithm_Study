import sys
inp = sys.stdin.readline
village = []
people = 0
for _ in range(int(inp())):
    a, b = map(int, inp().split())
    village.append([a, b])
    people += b
village.sort(key=lambda x:x[0])
cnt = 0
for i, p in village:
    cnt += p
    if cnt >= people/2:
        print(i)
        break
