import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
num = list(map(int, inp().split()))
op = list(map(int, inp().split()))
## max는 -sys.maxsize로 설정해야 max가 음수일 때도 반영
res_max, res_min = -sys.maxsize, sys.maxsize
def operate(k, res):
    global res_max, res_min
    if k == N-1:
        res_max = max(res, res_max)
        res_min = min(res, res_min)
        return
    for i in range(4):
        if op[i]:
            temp = res
            if i == 0:
                res += num[k+1]
            elif i == 1:
                res -= num[k+1]
            elif i == 2:
                res *= num[k+1]
            else:
                if res >= 0:
                    res //= num[k+1]
                else:
                    res = (-res // num[k+1]) * (-1)
            op[i] -= 1
            operate(k+1, res)
            op[i] += 1
            res = temp
operate(0, num[0])
print(res_max)
print(res_min)