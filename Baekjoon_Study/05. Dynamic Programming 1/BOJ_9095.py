import sys
inp = sys.stdin.readline
## n은 10 이하의 양의 정수 -> 사이즈 11인 리스트
count = [0] * 11
test = [int(inp()) for _ in range(int(inp()))]
count[1] = count[0] = 1
def dp(n):
    if count[n]:
        return count[n]
    if n >= 3:
        count[n] += dp(n-3)
    if n >= 2:
        count[n] += dp(n-2)
    count[n] += dp(n-1)
    return count[n]
for t in test:
    print(dp(t))