import sys
inp = lambda : sys.stdin.readline()
N = int(inp())
students = sorted(map(int, inp().split()))
res = 0
for i in range(N-2):
    selected = students[i]
    if selected > 0: break
    left, right = i + 1, N - 1
    while left < right:
        s_sum = selected + students[left] + students[right]
        if s_sum < 0:
            left += 1
        elif s_sum > 0:
            right -= 1
        else :
            ## 0인 경우
            if students[left] == students[right]:
                # nC2
                res += (right - left + 1) * (right - left) // 2
                break
            else:
                r = 0
                # 같을 때 까지 이동
                while students[right] == students[right - r]:
                    r += 1
                right -= r

                l = 0
                # 같을 때 까지 이동
                while students[left] == students[left + l]:
                    l += 1
                left += l

                res += l * r
print(res)