import sys
inp = lambda: sys.stdin.readline().split()
A, B = map(int, inp())
# A 이상 B 이하인 수 중에 4와 7로만 이루어진 수 구하기
res = 0
## dfs를 이용한 풀이
def dfs(n):
    global res
    if A <= n <= B:
        res += 1
    if n > B:
        return

    dfs(10 * n + 4)
    dfs(10 * n + 7)
dfs(0)
print(res)
## bfs를 이용한 풀이
# q = deque([4, 7])
# while q:
#     t = q.popleft()
#     if t >= A:
#         if t > B:
#             break
#         else:
#             res += 1
#     q.append(t * 10 + 4)
#     q.append(t * 10 + 7)