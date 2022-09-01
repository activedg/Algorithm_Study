# Using Stack
n = int(input())
test, stack = [], []
res = [True] * n
for _ in range(n):
    test.append(input())
for i in range(n):
    for j in range(len(test[i])):
        if test[i][j] == '(':
            stack.append(1)
        else:
            if not stack:
                res[i] = False
                break
            stack.pop()
    if res[i] and not stack:
        res[i] = True
    else: res[i] = False
    stack.clear()
for i in range(len(res)):
    print("YES") if res[i] else print("NO")

# Not using Stack
N = int(input())
for _ in range(N):
    a = input()
    while "()" in a:
        a = a.replace("()", "")
    if len(a) == 0:
        print("YES")
    else: print("NO")