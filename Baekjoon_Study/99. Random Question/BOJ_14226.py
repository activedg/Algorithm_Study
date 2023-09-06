import sys
from collections import deque
inp = lambda : sys.stdin.readline()
# 화면에 있는 이모티콘 모두 복사해서 클립보드에 저장
# 클립보드에 있는 모든 이모티콘 붙여넣기
# 화면에 있는 이모티콘 중 하나 삭제
S = int(inp())
# 이모티콘 현재 개수 1개
q = deque()
q.append((1, 0))

visited = dict()
visited[(1, 0)] = 0

while q:
    cur, clip = q.popleft()

    if cur == S:
        print(visited[(cur, clip)])
        break

    for path in ((cur, cur), (cur + clip, clip), (cur -1, clip)):
        if path not in visited:
            visited[path] = visited[(cur, clip)] + 1
            q.append(path)
# res = sys.maxsize
# visited = [[-1 for _ in range(S+1)] for _ in range(S+1)]
# visited[1][0] = 0
# while q:
#     cur, clip = q.popleft()
#
#     if cur != clip and visited[cur][cur] == -1:
#         visited[cur][cur] = visited[cur][clip] + 1
#         q.append((cur, cur))
#
#     if cur + clip <= S and visited[cur + clip][clip] == -1:
#         visited[cur + clip][clip] = visited[cur][clip] + 1
#         q.append((cur + clip, clip))
#
#     if cur > 1 and visited[cur - 1][clip] == -1:
#         visited[cur - 1][clip] = visited[cur][clip] + 1
#         q.append((cur - 1, clip))
#
# res = min(s for s in visited[S] if s != -1)
# print(res)