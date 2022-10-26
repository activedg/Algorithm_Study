import sys
inp = lambda : int(sys.stdin.readline())
number = { 2 : 1, 3 : 7, 4 : 4, 5 : 2, 6 : 0, 7: 8, 8: 10}
dp = [sys.maxsize] * 101
for key, val in number.items():
    dp[key] = val
dp[6] = 6
# 예 : 7이 들어왔을 때 -> 최대 711 최소 8
def max_stick(k):
    temp = ''
    if k % 2:
        temp += '7'
        k -= 3
    temp += '1' * (k // 2)
    return int(temp)
def min_stick(k):
    if dp[k] != sys.maxsize:
        return dp[k]
    ## 7개가 남으면 8, 6개가 남으면 0
    ## dp[8] = 10, dp[15] = dp[8]과 dp[7] 합침, dp[14] = 88, dp[16] = 188 ->
    else:
        for i in range(9, k+1):
            if dp[i] != sys.maxsize: continue
            for j in range(2, 9):
                dp[i] = min(dp[i], int(str(dp[i - j]) + str(number[j])))
        return dp[k]
for _ in range(inp()):
    n = inp()
    # 1, 2/ 2, 5/ 3, 5/ 4, 4/ 5, 5/ 6, 6/ 7, 3/ 8, 7/ 9, 6/ 0, 6
    ## 성냥개비 모두 사용해야함
    ## 자리 수가 더 우선 적으로 생각
    ## 0으로 시작할 수 없음
    print(min_stick(n), max_stick(n))