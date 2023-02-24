# 01 Knapsack
배낭에 일정 가치와 무게가 있는 짐들을 넣는데 해당 짐을 쪼개서 넣을 수 없는 문제이다.
01 Knapsack은 동적계획법으로 풀 수 있다.

## 문제 접근 방법
- 기존의 DP문제와 같이 큰 문제를 작은 문제로 나눌 수 있는지 생각해본다. 
- dp 배열을 무엇을 기반으로 선언할 지도 매우 중요하다.
  - 2차원 배열로 할지
  - 인덱스는 무엇으로 할지(ex. 배낭 무게 등)
- 1번째 인덱스부터가 아닌 역순으로 접근하는 경우도 꽤 있다. 

## 그림
<img width="768" alt="image" src="https://user-images.githubusercontent.com/70252417/217566868-0ac02e3c-4e19-4fe6-82b3-e064683f58b7.png">
<img width="768" alt="스크린샷 2023-02-09 오전 12 01 03" src="https://user-images.githubusercontent.com/70252417/217568319-10372eb4-ac49-490f-b162-543dd216ce55.jpg">
<img width="442" alt="스크린샷 2023-02-09 오전 12 01 03" src="https://user-images.githubusercontent.com/70252417/217567521-75ea8b79-b4d6-480d-95a4-b04016d5101e.png">

- i 번째 까지 포함한 것들 중 i가 포함된 경우 or 포함되지 않은 경우로 나눠서 생각한다.
- dp[i][w]에서 w는 무게로 접근하였다.


## 예제) 백준_12865 평범한 배낭
```python
import sys
inp = lambda : sys.stdin.readline().split()
N, K = map(int, inp())
items = [list(map(int, inp())) for _ in range(N)]
# 물건을 1~i까지만 고려하고 (임시) 배낭 용량이 w일 때 최대 가치
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
# 무게, 가치 순
for i in range(1, N+1):
    for j in range(1, K+1):
        w = items[i-1][0]
        # 물건 i의 무게가 임시 용량 초과시
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], items[i-1][1] + dp[i-1][j-w])
print(dp[N][K])
```
---
# LCS(Longest Common Subsequence)
DP를 활용하여 가장 공통되는 부분 문자열을 구할 수 있다.
<img width="733" alt="image" src="https://user-images.githubusercontent.com/70252417/221196748-1fbcb91e-48ff-4ecc-bced-d3c52dc27ff4.png">
