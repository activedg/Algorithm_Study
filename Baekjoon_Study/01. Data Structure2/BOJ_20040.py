import sys
inp = lambda : sys.stdin.readline().split()
# 사이클이 완성되면 겜 종료
## 사이클 완성되는 조건이 중요할듯
# 어느 세 점도 일직선 위에 없음 => 서로 공통된 원소가 없는 집합
n, m = map(int, inp())
reps = list(range(n))
def find(r):
    if reps[r] != r:
        r = find(reps[r])
    return reps[r]
def union(node1, node2):
    r1 = find(node1)
    r2 = find(node2)
    if r1 < r2:
        reps[r2] = r1
    else:
        reps[r1] = r2

for i in range(1, m+1):
    x, y = map(int, inp())
    rep_x, rep_y = find(x), find(y)
    # 이미 같은 그룹에 있는 애들 끼리 union 하는 것이면 사이클이 생성된 거라 간주
    if rep_x == rep_y:
        print(i)
        exit()
    # 두 점을 이어 하나의 집합으로 합치기
    union(x, y)
print(0)