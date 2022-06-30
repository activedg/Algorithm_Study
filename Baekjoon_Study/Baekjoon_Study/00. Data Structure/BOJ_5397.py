from collections import deque
import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline() for _ in range(N)]
for s in data:
    # 스택 두 개 사용, 마우스 커서 기준 왼쪽 -> 왼쪽 스택, 오른쪽 -> 오른쪽 스택
    stack_left, stack_right = deque([]), deque([])
    for c in s:
        if c.isalnum():
            stack_left.append(c)
        elif stack_left and c == '<':
            stack_right.appendleft(stack_left.pop())
        elif stack_right and c == '>':
            stack_left.append(stack_right.popleft())
        elif stack_left and c == '-':
            stack_left.pop()
    print(''.join(stack_left) + ''.join(stack_right))
