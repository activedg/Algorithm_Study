import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
people = list(map(int, inp().split()))
res = 0
start, end = 0, N-1
while start + 1 < end:
    res = max(res, min(people[start], people[end]) * (end - start - 1))
    ## start 포인터가 가리키는 값이 더 작으면 start 포인터 값을 이동시켜 사이에 있는 인원을 줄이지만 min 값을 크게 한다.
    if people[start] < people[end]:
        start += 1
    else:
        end -= 1
print(res)