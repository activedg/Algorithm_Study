import sys
from math import sqrt
inp = lambda : int(sys.stdin.readline())
# 소수로만 지불해야함
## 자기 이하인 소수 리스트 만들기
def is_prime(num):
    if num < 2: return False
    for i in range(2, int(sqrt(num)) + 1):
        if not num % i:
            return False
    return True
N = inp()
primes = [p for p in range(2, N+1) if is_prime(p)]
dp = [0] * (N+1)
dp[0] = 1
# 소수 별로 사용 했을 때 dp값 갱신
for p in primes:
    for i in range(p, N+1):
        dp[i] = (dp[i] + dp[i-p]) % 123456789
print(dp[-1])