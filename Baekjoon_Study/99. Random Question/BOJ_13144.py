import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
nums = list(map(int, inp().split()))
# 숫자 길이가 최대 100000개 => 일일이 조합하는 건 아닐듯
start, end = 0, 0
# bool 자료형으로 안하고 가진 갯수로 체크
check = [0] * 100001
res = 0
while end < N:
    # 우측 포인터 원소 값이 중복됬는지
    if not check[nums[end]]:
        check[nums[end]] += 1
        end += 1
    else:
        res += (end - start)
        check[nums[start]] -= 1
        start += 1
# while 문 이후에 남은 것들로 만들 수 있는 경우의 수
res += ((end - start) * (end - start + 1)) // 2
print(res)
