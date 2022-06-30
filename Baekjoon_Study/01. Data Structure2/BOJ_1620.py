import sys
N, M = map(int, sys.stdin.readline().split())
data = {}
arr = [0]
for i in range(N):
    temp = sys.stdin.readline().rstrip()
    data[temp] = i + 1
    arr.append(temp)
for _ in range(M):
    inst = sys.stdin.readline().rstrip()
    if inst.isdigit():
        print(arr[int(inst)])
    else:
        print(data[inst])