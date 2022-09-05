# 04. 그리디
- 그리디 알고리즘으로 얻는 해가 최적의 해(예. 정렬된 상황)가 되는 상황 -> 이를 추론해야 함
- 최대한 어떤 행동을 취하기 (예. 나누기, 곱하기, 혹은 선택) // 정당성 분석 단계
- 현재 상태에서 조건이 맞다면 A를 수행 아니면 B를 수행하는 방식으로 최적의 해를 구하는 방식

:bulb: **최적의 해를 도출 할 수 있는 상황(예. 정렬된 상황)을 찾고 조건 비교를 하며 반복문(for문 혹은 투 포인터 활용 while문) 돌리기** 

## 예제) 모험가 길드문제
한 마을에 모험가 N명, 공포도가 X인 모험가는 반드시 X명 이상으로 구성된 모험가 그룹으로 가야한다. 또한 모든 사람이 다 갈 필요 없다.
여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 문제

### 풀이 방법
인풋으로 받은 리스트를 정렬 시킨 후 반복문을 돌며 카운트의 값이 f값 이상으로 되면 여행을 보내 최대한 많이 보내는 문제이다. 정렬 시킴으로써 최적의 해를 구할 수 있는 상황을 만들고 
for문을 돌며 조건을 확인 하여 값을 구한다.

```python
import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
fear = sorted(map(int, inp().split()))
count, res = 0, 0
# 1 2 2 2 3
for f in fear:
    count += 1
    if f <= count:
        res += 1
        count = 0
print(res)
```

## 예제) 백준 20300번 문제
운동기구를 PT를 받을 때 마다 2개씩 사용하며 이때 이전에 사용하지 않은 기구들을 이용한다. 근손실 정도의 최솟값을 구한다.

### 풀이 방법
먼저 인풋 리스트를 정렬한 후 N값이 홀수 인 경우 가장 근손실 정도가 큰 기구는 마지막 날 하나만 사용하도록 한다. 정렬된 리스트에서 투 포인터를 사용하여
현재 검색하는 리스트에서 최솟값, 최댓값을 합하여 근손실 정도를 가장 낮추는 방향으로 while문을 돌렸다. 
```python
import sys
inp = sys.stdin.readline
N = int(inp())
T = sorted(list(map(int, inp().split())))
res = 0
if N % 2:
    res = T[-1]
    T.pop()
left, right = 0, len(T)-1
while left < right:
    res = max(res, T[left] + T[right])
    left += 1
    right -= 1
print(res)
```
