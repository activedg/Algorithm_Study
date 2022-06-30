import sys
in_str = sys.stdin.readline()
stack, res, temp = [], 0, 1
for i in range(len(in_str)):
    if in_str[i] == '(':
        stack.append(in_str[i])
        temp *= 2
    elif in_str[i] == '[':
        stack.append(in_str[i])
        temp *= 3
    elif in_str[i] == ')':
        if stack and stack[-1] == '(':
            if in_str[i-1] == '(':
                res += temp
            stack.pop()
            temp /= 2
        else:
            res = 0
            break
    elif in_str[i] == ']':
        if stack and stack[-1] == '[':
            if in_str[i-1] == '[':
                res += temp
            stack.pop()
            temp /= 3
        else:
            res = 0
            break
if stack:
    res = 0
print(int(res))