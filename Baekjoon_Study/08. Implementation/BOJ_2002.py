import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
# N 개의 차량 지나가는 것 기록
## a b c d
## d a b c
## 2가 나와야 정상
### 1보다 3이 먼저 나왔기 때문에 3도 추월한 거
car_dict = {}
car_out = []
for i in range(N):
    car_dict[inp()] = i
car_out = [inp() for _ in range(N)]
res = 0
for i in range(N-1):
    for j in range(i+1, N):
        # 먼저 나간 차보다 순번이 낮은게 있는지 체크 => 추월 한 것임
        if car_dict[car_out[i]] > car_dict[car_out[j]]:
            res += 1
            break
print(res)