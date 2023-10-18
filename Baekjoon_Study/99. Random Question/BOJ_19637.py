import sys, bisect
inp = lambda : sys.stdin.readline()
# 캐릭터가 가진 전투력 기준으로 칭호 붙여줌
# 칭호의 개수 N, 칭호를 출력해야 하는 캐릭터들의 개수 M
# 전투력 상한값 주어짐
N, M = map(int, inp().split())
# 비 내림차순으로 주어짐
awards = []
fights = []
for _ in range(N):
    award, fight = map(str, inp().split())
    awards.append(award)
    fights.append(int(fight))
for _ in range(M):
    fight = int(inp())
    idx = bisect.bisect_left(fights, fight)
    print(awards[idx])
