import sys
inp = lambda : sys.stdin.readline()
# 마을을 이루고 있는 집의 개수 N, 도둑이 돈을 훔쳐 할 연속된 집의 개수 M
# 자동 방범장치 작동하는 최소 돈 K원
## 연속된 M개의 집 털어 최대 K-1원까지
for _ in range(int(inp())):
    N, M, K = map(int, inp().split())
    house = list(map(int, inp().split()))
    # 첫 번째 집과 마지막 집 연결되어 있음
    # 슬라이딩 윈도우 기법 사용
    temp = sum(house[:M])
    res = 0 if temp >= K else 1
    # M과 N이 같은 경우 for문 건너뛰기
    if N != M:
        for i in range(1, N):
            temp += house[(i + M - 1) % N] - house[i-1]
            if temp < K: res += 1
    print(res)