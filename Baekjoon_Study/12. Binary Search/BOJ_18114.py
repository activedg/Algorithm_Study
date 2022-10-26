import sys
inp = lambda : sys.stdin.readline().split()
N, C = map(int, inp())
items = sorted(map(int, inp()))
## 4 15
## 3 5 6 7
# 최대 3개까지 선택해서 C의 무게에 딱 맞게 가져오면 됨
## 한 개 먼저 배제해보기
if C in items:
    print(1)
else:
    ## 두 개 부터 시작
    start, end = 0, N-1
    while start < end:
        mid = items[start] + items[end]
        if mid == C:
            print(1)
            exit(0)
        elif mid < C:
            if end - start > 1 and C - mid in items[start+1:end]:
                print(1)
                exit(0)
            else:
                start += 1
        else:
            end -= 1
    print(0)