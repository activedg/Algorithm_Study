import sys
inp = lambda : map(int, sys.stdin.readline().split())
N, X = inp()
visit = list(inp())
if max(visit) == 0:
    print("SAD")
else:
    temp_max = sum(visit[:X])
    res, cnt = temp_max, 1
    for i in range(X, N):
        temp_max = temp_max + visit[i] - visit[i - X]
        if temp_max > res:
            res = temp_max
            cnt = 1
        elif temp_max == res:
            cnt += 1
    print(res)
    print(cnt)
## defaultdict 사용하는 방법
# from collections import defaultdict

# def_dict = defaultdict(int)
# for i in range(1, N):
#     visit[i] += visit[i-1]
# i = 0
# for j in range(X-1, N):
#     temp = visit[j] - visit[i-1] if i else visit[j]
#     def_dict[temp] += 1
#     i += 1
# s = sorted(def_dict.items(), reverse=True)
# if s[0][0]:
#     print(s[0][0])
#     print(s[0][1])
# else:
#     print('SAD')