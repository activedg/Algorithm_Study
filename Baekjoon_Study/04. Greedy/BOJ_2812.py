import sys
inp = lambda : sys.stdin.readline()
## 4177252841
N, K = map(int, inp().split())
number = list(map(int, inp().rstrip()))
stack = []
# 새로 들어 올려는 애가 기존의 값 보다 크면 -> stack.pop// 4/ 4, 1/ [] / 7/ 7 7/ 7 7 2/ 7 7 5/ 7 7 5 2/ 7 7 5 8
## 스택을 이용 하여 현재 값과 스택 값을 비교하여 pop하기
for n in number:
    while stack and stack[-1] < n and K > 0:
        K -= 1
        stack.pop()
    stack.append(n)
if K > 0:
    stack = stack[:-K]
print(''.join(map(str, stack)))