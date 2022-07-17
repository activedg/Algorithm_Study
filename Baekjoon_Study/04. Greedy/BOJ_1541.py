import sys
inp = sys.stdin.readline
## - 기준으로 괄호를 치면 최솟값이 나온다
t = inp().rstrip().split('-')
res = 0
for i, x in enumerate(t):
    temp = sum(map(int, x.split('+'))) if '+' in x else int(x)
    res = res - temp if i != 0 else temp
print(res)
# t = re.split('([+|-])', inp().rstrip())
# change = False
# for i in range(len(t)):
#     if t[i] == '-':
#         change = True
#     elif change and t[i] == '+':
#         t[i] = '-'
# res = int(t[0])
# i = 1
# while i < len(t):
#     if t[i] == '+':
#         res += int(t[i+1])
#         i += 2
#     elif t[i] == '-':
#         res -= int(t[i+1])
#         i += 2
# print(res)