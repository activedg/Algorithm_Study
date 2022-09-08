import sys
from collections import deque, defaultdict
# deque, dict 자료형을 제대로 사용할 수 있는지 체크하는 문제
inp = lambda : sys.stdin.readline()
N, M = map(int, inp().split())
## P : 상위 폴더의 이름/ F : 폴더 또는 파일의 이름/ C : 폴더 인지 아닌지
directory = defaultdict(list)
for _ in range(N+M):
    P, F, C = map(str, inp().split())
    directory[P].append((F, int(C)))
for _ in range(int(inp())):
    s = list(inp().rstrip().split('/'))
    ## s[-1] 값 -> 해당 디렉토리 탐색
    file_set, cnt = set(), 0
    folder_q = deque([s[-1]])
    ## bfs와 유사한 방식으로 탐색
    while folder_q:
        fo = folder_q.popleft()
        for f, c in directory[fo]:
            if not c:
                file_set.add(f)
                cnt += 1
            else:
                folder_q.append(f)
    print(len(file_set), cnt)