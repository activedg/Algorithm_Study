import sys
inp = lambda : sys.stdin.readline().rstrip()
# 인접해 있는 모든 문자가 같지 않은 문자열 => 행운의 문자열
# 원래 문자열이 행운의 문자열이면 그것도 개수에 포함됨
s = inp()
alpha = dict()
for a in list(s):
    try: alpha[a] += 1
    except: alpha[a] = 1
keys = alpha.keys()
N = len(alpha)
res = 0
## 일반 순열 사용했을 때 메모리 초과 발생 => 백트래킹으로 되는지 확인!
def dfs(depth, path=[]):
    if depth == len(s):
        global res
        res += 1
        return

    for k in keys:
        if alpha[k] > 0:
            if len(path) >= 1 and path[-1] == k: continue
            alpha[k] -= 1
            dfs(depth + 1, path + [k])
            alpha[k] += 1
dfs(0)
print(res)