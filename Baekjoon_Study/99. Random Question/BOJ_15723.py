import sys
from collections import defaultdict, deque
inp = lambda : sys.stdin.readline().rstrip()
# N개의 줄에 해당 하는 것 일일이 추가하기
demon_dict = defaultdict(list)
for _ in range(int(inp())):
    a, _, b = map(str, inp().split())
    demon_dict[a].append(b)
for _ in range(int(inp())):
    a, _, b = map(str, inp().split())
    # deque로 일일이 조건 체크하면서 가능한지 판단
    q = deque([a])
    visit = defaultdict(bool)
    check = False
    while q:
        x = q.popleft()
        if x == b:
            check = True
            break
        for d in demon_dict[x]:
            if not visit[d]:
                visit[d] = True
                q.append(d)
    print('T') if check else print('F')