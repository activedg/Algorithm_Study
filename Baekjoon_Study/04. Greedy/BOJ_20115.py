import sys
inp = sys.stdin.readline
N = int(inp())
X = sorted(list(map(int, inp().split())))
res = X[-1] + sum( x/2 for x in X[:-1])
print(res) if res % 1 else print(int(res))
# sort 없이(4번 라인에서 sorted 없이) print((max(X) + sum(X))/2) 로도 가능