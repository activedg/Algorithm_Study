import sys
inp = lambda : sys.stdin.readline().rstrip()
# N일 동안 M번만 통장에서 돈을 빼서 쓰기로 함
# 통장에서 K원 인출 => 하루 보낼 수 있으면 그대로 사용, 모자라면 남은 금액 통장에 집어넣기
## 남은 금액이 그날 사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원 인출 가능
# M번 인출하는 것을 맞추면서 K 최소화
N, M = map(int, inp().split())
money = [int(inp()) for _ in range(N)]
start, end = max(money), sum(money)
res = end
while start <= end:
    mid = (start + end) // 2
    cnt, temp = 1, mid
    for m in money:
        if temp < m:
            temp = mid - m
            cnt += 1
        else:
            temp -= m
    if cnt > M:
        start = mid + 1
    else:
        # cnt 개수가 M보다 적으면 cnt를 M으로 맞추기 위한 작업 가능
        res = mid
        end = mid - 1
print(res)