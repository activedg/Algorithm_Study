import sys
in_str = sys.stdin.readline().replace('()', 'L')
stack = []
count = 0
for c in in_str:
    if c == '(':
        stack.append(1)
    elif c == ')':
        stack.pop()
        count += 1
    else:
        count += len(stack)
print(count)
