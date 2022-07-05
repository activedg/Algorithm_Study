import sys
inp = sys.stdin.readline
n = int(inp())
cnt = 0
while True:
    if not n % 5:
        cnt += n // 5
        break
    else:
        n -= 2
        cnt += 1
    if n < 0:
        cnt = 0
        break
print(cnt) if cnt else print(-1)
## 기존 풀이
# n = int(inp())
# if n > 5 and n % 5 % 2: cnt = n//5 - 1
# else: cnt = n//5
# n -= cnt * 5
# cnt += n // 2
# n %= 2
# print(cnt) if cnt and not n else print(-1)