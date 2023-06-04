import sys
inp = lambda : sys.stdin.readline()
# 루트 땅번호 1
# 땅의 번호 K -> 왼쪽 자식 땅의 번호 2 x K, 오른쪽 자식 번호 2 x K + 1
# 오리가 원하는 땅까지 가는 길에 이미 다른 오리가 점유한 땅 있다면 오리 땅 가지지 못함
## 각 오리별로 원하는 땅 가질 수 있는지, 가질 수 없다면 처음 마주치는 점유된 땅 번호 구하기
N, Q = map(int, inp().split())
ducks = [int(inp()) for _ in range(Q)]
owns = [False for _ in range(N+1)]
for i in range(Q):
    # 타겟에서 부터 루트 노드까지 있는지 점유된 땅 있는지 파악
    target = ducks[i]
    res = 0
    while target > 1:
        if owns[target]:
            res = target
        target = target // 2

    if res:
        print(res)
    else:
        owns[ducks[i]] = True
        print(0)