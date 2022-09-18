# 완전 탐색
>문제를 해결 하기 위해 확인해야 하는 모든 경우를 탐색하는 방법

백 트래킹을 통해야 해결하는 문제 연습해보기

N개 중 중복을 허용/ 중복 없이 M개 순서 없이/ 순서 있게 나열 하기 문제가 대표적 문제

<b>모든 코테 문제에서 인풋의 사이즈가 작으면 기본적으로 접근해보기</b>

# 백트래킹
>현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

<b>재귀(dfs 방식)를 사용하며 탐색! 백트래킹은 상태를 넘나드며 탐색한다고 생각하면 됨</b>

문제의 숫자 및 인풋값 제한을 확인하고 백트래킹으로 풀수 있는지 확인!! 

## 백준 예제) 14888번 문제
사칙 연산자들을 숫자들 사이에 끼워 넣는 방식이다. 중복을 허용하지 않는 순열이라 생각하여 문제를 접근하였다.

### 문제 풀이 방법
먼저 종료 조건을 만들어 주었다. dfs에서 depth == k와 같은 느낌이라고 보면된다. 즉, 더이상 넣을 연산자가 없는 상황을 말한다. 문제에 따라 
종료 조건이 애매해 마지막에 넣어 최댓값, 최솟값을 비교하는 문제도 있다.
```python
 if k == N-1:
        res_max = max(res, res_max)
        res_min = min(res, res_min)
        return
```
사칙연산 별로 케이스를 나누어 계산하되, 나누기 연산의 경우만 양수로 바꾼 뒤 연산 후 다시 -를 붙여준다.
```python
import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
num = list(map(int, inp().split()))
op = list(map(int, inp().split()))
## max는 -sys.maxsize로 설정해야 max가 음수일 때도 반영
res_max, res_min = -sys.maxsize, sys.maxsize
def operate(k, res):
    global res_max, res_min
    if k == N-1:
        res_max = max(res, res_max)
        res_min = min(res, res_min)
        return
    for i in range(4):
        if op[i]:
            temp = res
            if i == 0:
                res += num[k+1]
            elif i == 1:
                res -= num[k+1]
            elif i == 2:
                res *= num[k+1]
            else:
                if res >= 0:
                    res //= num[k+1]
                else:
                    res = (-res // num[k+1]) * (-1)
            op[i] -= 1
            operate(k+1, res)
            op[i] += 1
            res = temp
operate(0, num[0])
print(res_max)
print(res_min)
```
