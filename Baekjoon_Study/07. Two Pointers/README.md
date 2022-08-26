# 07. Two Pointers
리스트에 순차적으로 접근 해야 할 때, 두개의 포인터를 이용해 위치를 기록하면서 처리하는 기법

<u> 문제에 따라 리스트의 정렬을 하고 할 수도 있고, 안하고 할 수도 있음 </u>

## 문제 풀이 기법
start, end(혹은 left, right)를 문제에 따라 적절히 둔다. 예를 들어, start는 리스트의 시작점 end는 리스트의 마지막 index로 초기화한다.
문제의 조건에 따라 start와 end를 움직여 가며 문제를 푼다. start를 for문의 index로 두고 end값을 변화 시키는 방법을 사용한다.


## 예시) 백준 2470번 문제 풀이
문제 : 산성 용액과 알칼리성 용액에 각각의 특성 값이 있다. 주어진 용액의 특성값들 중에 두 용액의 특성값을 합하여 0에 가장 가깝게 되는 두 용액의 특성값을 출력한다.
### 접근 사고
0에 가깝게 만들려면 음수와 양수를 더하는 경우가 가장 답에 가깝게 되므로 인풋을 받을 때 정렬을 먼저하였다.

```python
inp = lambda : sys.stdin.readline().rstrip()
N = int(inp())
sol = sorted(list(map(int, inp().split())))
l, r = 0, N - 1
res = [sol[l] + sol[r], l, r]
```

반복문을 도며 처음으로 할 행동은 현재 left, right 포인터가 가리키는 값들을 더한 값(temp의 절댓값)과 저장된 최댓값(res[0]의 절댓값)과의 비교이다.
```python
while l < r:
    temp = sol[l] + sol[r]
    if abs(temp) < abs(res[0]):
        res = [temp, l, r]
```

이후 temp값이 만약 0보다 작으면 left 포인터를 1만큼 증가시키고 0보다 크면 right 포인터를 1만큼 감소시킨다.
```python 
    if temp < 0:
        l += 1
    else:
        r -= 1
```
반복문이 끝난 후 res에 저장된 left, right 포인터가 가리키는 값을 출력한다.

## 정리
반복문을 돌며 문제에 필요한 비교조건을 먼저 확인한 후, 현재 값에 따라 start(left) 혹은 end(right)포인터를 이동시킨다.
