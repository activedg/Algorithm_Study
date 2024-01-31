# Softeer_징검다리
- 난이도 : 레벨 3
- 문제 : https://softeer.ai/practice/6293/PRACTICE/try

## 접근 방법
가장 긴 증가하는 부분 수열과 비슷한 문제이다. 징검다리 건너는 돌이 연속하지 않아도 된다.
dp 풀이법을 사용하고자 하였는데, 매 번 자신이 마지막 돌이라 생각하고 계산을 한다.
직전까지 돌 중, 자신 보다 작은 것이 있다면 해당 돌의 dp값에 1을 추가하고 max 연산을 취해준다.
자신보다 작은 것이 없는 경우도 있을 수 있기 때문에, 반복문을 돌 때 직전 값으로 대입해 주었다.

## 코드
```python
import sys 
inp = lambda : sys.stdin.readline()
# 징검다리 돌 높이 모두 다름
# 서 -> 동으로 점점 높은 돌을 밟으면서 개울 지나려함
# 밟을 수 있는 돌의 최대 개수
## 3 2 1 4 5
N = int(inp())
A = list(map(int, inp().split()))
dp = [0] * N
for i in range(N):
    dp[i] = 1
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
```