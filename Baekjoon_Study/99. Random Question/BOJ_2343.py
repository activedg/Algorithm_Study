import sys
inp = lambda : sys.stdin.readline().split()
N, M = map(int, inp())
arr = list(map(int, inp()))
# i번과 j번 블루레이를 같은거에 녹화할려면 그 사이꺼도 다 넣어야함
# 블루레이 크기 최소화 => 블루레이 크기를 구해야 함
# 블루레이 개수를 신경쓰지 않을 때의 최대 크기 = 전체 강의를 하나의 블루레이에 다 넣을 때
right = sum(arr)
# 블루레이 개수를 신경쓰지 않을 때의 최소 크기 = 전체 강의 중 가장 긴 강의
# 블루 레이 개수가 무한개라면, 최소 크기는 전체 강의 중 가장 긴 강의가 되야 한다.
left = max(arr)
res = right
while left <= right:
    # mid 값은 블루레이 길이
    mid = (left + right) // 2
    # cnt는 블루레이 개수, temp는 블루레이 길이
    cnt, temp = 1, 0
    for a in arr:
        if temp + a <= mid:
            temp += a
        # mid보다 커지면 블루레이 개수 늘리기
        else:
            temp = a
            cnt += 1
    if cnt <= M:
        right = mid - 1
        res = min(res, mid)
    else:
        left = mid + 1
print(res)
