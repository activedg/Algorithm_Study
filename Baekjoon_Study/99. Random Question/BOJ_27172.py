import sys
inp = lambda : sys.stdin.readline()
# 수 나누기 게임
# 게임 시작 전 각 플레이어는 1부터 백만 사이 수가 적힌 서로 다른 카드 잘 섞은 뒤 한 장씩 나눠가짐
# 매턴마다 다른 플레이어와 결투
# 서로 카드 보여주는 방식
## 플레이어 수로 다른 플레이어 수 나눴을 때 나머지 0이면 승리
## 반대로 나누어지면 패배
## 둘다 아니라면 무승부
# 승리한 플레이어 1점, 패배한 플레이어 -1점
# 본인 제외 모든 플레이어와 한 번씩 결투
N = int(inp())
cards = list(map(int, inp().split()))
cards_max = max(cards)
checker, score = [False] * (cards_max + 1), [0] * (cards_max + 1)
for card in cards:
    checker[card] = True
# 조합론으로 문제 풀면 시간 초과
for x in cards:
    for y in range(x * 2, cards_max + 1, x):
        # 자신의 카드의 배수가 존재
        if checker[y]:
            score[x] += 1
            score[y] -= 1

print(*[score[card] for card in cards])