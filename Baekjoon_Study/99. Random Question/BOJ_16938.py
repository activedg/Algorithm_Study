import sys
inp = lambda : sys.stdin.readline().split()
# 문제는 총 N개, 캠프에 사용할 문제 두 문제 이상
# 문제 난이도 합은 L보다 크거나 같고 R보다 작아야 함
# 가장 어려운 문제와 쉬운 문제 난이도 차이 X 이상
## 문제 개수 1개 부터 15개 => depth 적으니 백 트래킹 해볼까?
## 문제를 포함하는 경우 + 포함하지 않는 경우
N, L, R, X = map(int, inp())
questions = sorted(map(int, inp()))
global res
res = 0
def dfs(depth, arr: list, arr_sum):
    global res
    if depth == N:
        if len(arr) < 2: return
        if max(arr) - min(arr) < X: return
        if arr_sum < L or arr_sum > R: return
        res += 1
        return
    dfs(depth + 1, arr + [questions[depth]], arr_sum + questions[depth])
    dfs(depth + 1, arr, arr_sum)
dfs(0, [], 0)
print(res)
