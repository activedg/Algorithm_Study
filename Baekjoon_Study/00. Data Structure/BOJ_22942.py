import sys
N = int(sys.stdin.readline())
data = []
for i in range(N):
    x, r = map(int, sys.stdin.readline().split())
    data.append([x-r, x+r])
# x[0] 기준으로 정렬
data.sort(key=lambda x:x[0])
stack = []
for s, e in data:
    # 시작점이 스택 top 의 종료점보다 뒤에 있을 때 (당연하게 접점 없는 것들 pop)
    while stack and stack[-1][1] < s:
        stack.pop()
    if stack:
        # 내접 or 접점 존재
        if stack[-1][1] <= e:
            print("NO")
            exit(0)
    stack.append([s, e])
print("YES")