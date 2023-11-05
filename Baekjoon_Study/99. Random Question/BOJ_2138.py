import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
# i번 스위치를 누르면 i-1, i, i+1 세 개의 전구 상태 바뀜
## 1번은 1,2번/ N번은 N-1, N번
# 최소 몇 번 눌러야 할지

# 전구 누르는 순서 상관 없음
# 그리디 -> i가 i-1번쩨 결정
cur = list(map(int, inp().rstrip()))
target = list(map(int, inp().rstrip()))

cur_copy = cur[:]
# 전구 스위치 전환
def switch(bulb, count):
    for i in range(1, N-1):
        if bulb[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulb[j] = 1 - bulb[j]

    # 마지막 전구 따로 처리
    if bulb[N-1] != target[N-1]:
        count += 1
        bulb[N-2] = 1 - bulb[N-2]
        bulb[N-1] = 1 - bulb[N-1]

    if bulb == target:
        return count
    else:
        return -1

# 첫 번째 스위치를 누르냐 안 누르냐 구분
if cur == target:
    print(0)
else:
    # 첫 번째 스위치 안 누르기
    res = switch(cur, 0)
    if res != -1:
        print(res)
    else:
        # 누른 버전도 추가
        cur_copy[0] = 1 - cur_copy[0]
        cur_copy[1] = 1 - cur_copy[1]
        res = switch(cur_copy, 1)
        print(res)