from collections import deque
import sys
N = int(sys.stdin.readline())
queue = deque([])
for temp in range(N):
    temp = sys.stdin.readline().split()
    if temp[0] == 'push':
        a = int(temp[1])
        queue.append(a)
    elif temp[0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif temp[0] == 'size':
        print(len(queue))
    elif temp[0] == 'empty':
        print(0) if queue else print(1)
    elif temp[0] == 'front':
        print(queue[0]) if queue else print(-1)
    elif temp[0] == 'back':
        print(queue[-1]) if queue else print(-1)
