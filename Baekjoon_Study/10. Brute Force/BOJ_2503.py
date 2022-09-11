import sys
from itertools import permutations
inp = lambda : sys.stdin.readline()
N = int(inp())
game = []
for _ in range(N):
    game.append(list(map(int, inp().split())))
## 111 부터 999까지 탐색하면서 맞는지 확인?
num = list(permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
res = 0
for i in range(len(num)):
    checker = True
    for n, s, b in game:
        n_digit = [n // 100, (n // 10) % 10, n % 10]
        i_digit = [i // 100, (i // 10) % 10, i % 10]
        s_temp, b_temp = 0, 0
        for n1, i1 in zip(n_digit, i_digit):
            if i1 in n_digit:
                if n1 == i1:
                    s_temp += 1
                else:
                    b_temp += 1
        if s_temp != s or b_temp != b:
            checker = False
            break
    if checker: res += 1
print(res)