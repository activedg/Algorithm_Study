import sys
inp = lambda : sys.stdin.readline().split()
# n 개의 트럭이 건너감
# 트럭의 순서는 바꿀 수 없음
# 다리 위에는 단지 w대의 트럭만 동시에 올라갈 수 있음
# 다리 길이는 w, 한 칸씩만 이동 가능
# 다리 위에 올라가 있는 트럭들의 무게 합 <=L
n, w, L = map(int, inp())
a = list(map(int, inp()))
# 다리 위에 어떤 게 올라가 있는지에 대한 정보
bridge = [0] * w
# 다리에 올라가 있는 무게, 개수
bridge_weight, bridge_cnt = 0, 0
# 시간, 인덱스
res, finish_cnt = 0, 0
while finish_cnt < n:
    if bridge[-1]:
        bridge_weight -= bridge[-1]
        bridge_cnt -= 1
        finish_cnt += 1

    bridge = [0] + bridge[:-1]

    if a and bridge_cnt < n and bridge_weight + a[0] <= L:
        bridge[0] = a.pop(0)
        bridge_weight += bridge[0]
        bridge_cnt += 1

    res += 1
print(res)
